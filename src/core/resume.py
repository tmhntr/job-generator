from dataclasses import dataclass, field
import json
from typing import List, Union
from bs4 import BeautifulSoup
import re

import numpy as np


TEMPLATE_SKILLS = "TEMPLATE_SKILLS"
TEMPLATE_PROJECT_1_TITLE = "TEMPLATE_PROJECT_1_TITLE"
TEMPLATE_PROJECT_1_DESCRIPTION = "TEMPLATE_PROJECT_1_DESCRIPTION"
TEMPLATE_PROJECT_2_TITLE = "TEMPLATE_PROJECT_2_TITLE"
TEMPLATE_PROJECT_2_DESCRIPTION = "TEMPLATE_PROJECT_2_DESCRIPTION"


@dataclass
class ProjectData:
    title: str
    description: str
    # link: str
    
class SkillsData:
    def __init__(self, data):
        self.skills = data

    def get_skill_relatededness_matrix(self):
        n = len(self.skills)
        m = np.zeros((n, n))
        for i, skill in enumerate(self.skills.keys()):
            for j, skill2 in enumerate(self.skills.keys()):
                if i == j:
                    m[i, j] = 1
                if skill2 in self.skills[skill].keys():
                    m[i, j] = self.skills[skill][skill2]
        return m

    def get_skill_match_vector(self, matches: list[str]) -> list[int]:
        v = [0] * len(self.skills)
        for i, skill in enumerate(self.skills.keys()):
            if skill.lower() in matches:
                v[i] = 1
        return v
    
    def get_text_matches(self, text: str, skills: list[str]) -> list[str]:
        matches = []
        for skill in skills:
            pat = re.compile("(\s+)" + skill.lower() + "((\s+)|([.,!?:;'\"\'-]))")
            # use regex to find the skill in the text, must be surrounded by whitespace or punctuation
            search = re.search(pat, text.lower())
            if search:
                matches.append(skill)
        return matches

    def get_skills(self, posting: str = "", limit: Union[int, None] = None) -> list[str]:
        if not posting:
            return list(self.skills.keys())[:limit] if limit else list(self.skills.keys())
        
        matches = self.get_text_matches(posting, self.skills)

        match_vector = self.get_skill_match_vector(matches)

        related_matrix = self.get_skill_relatededness_matrix()

        value_vec = np.matmul(related_matrix, match_vector)

        conditioning_steps = 3
        for i in range(conditioning_steps):
            value_vec = np.matmul(related_matrix, value_vec)

        indices = np.argsort(value_vec)[::-1]
        for i in indices:
            if limit and len(matches) >= limit:
                break
            if list(self.skills.keys())[i] not in matches:
                matches.append(list(self.skills.keys())[i])
        
        if limit and len(matches) > limit:
            matches = matches[:limit]
        
        return matches
    
@dataclass
class ResumeData:
    name: str = ""
    email: str = ""
    website: str = ""
    address: str = ""
    projects: List[ProjectData] = field(default_factory=lambda: [])
    posting: str = ""
    skills: List[str] = field(default_factory=lambda: [])



class Resume:
    skills_limit: int = 6

    def __init__(self, html_template_file: str, data_file: str, posting_text: str = "", css_file: str = ""):
        with open(data_file, 'r') as f:
            data = json.load(f)
        self.skills_data = SkillsData(data['skills_relatedness'])
        projects = [ProjectData(**project) for project in data['projects']]
        self.data = ResumeData(projects=projects, posting=posting_text, **data['resume'])

        # read the html file to a variable
        with open(html_template_file, 'r') as f:
            html = f.readlines()
            
        self.html_template = "".join(html)

        if css_file:
            with open(css_file, 'r') as f:
                self.css = "".join(f.readlines())

    def set_skills(self, skills: list[str]):
        self.data.skills = skills

    def get_skills(self):
        return self.data.skills

    def set_posting(self, posting: str):
        self.data.posting = posting
        self.set_skills(self.skills_data.get_skills(posting, self.skills_limit))

    def get_posting(self):
        return self.data.posting



    def skill_string(self, skills: list[str]):
        s = ""
        if skills:
            for skill in skills:
                s += f"{skill}, "
            s = s[0].upper() + s[1:-2] + "."
        return s

    def get_soup(self):
        html = self.html_template
        html = re.sub(TEMPLATE_SKILLS, self.skill_string(self.data.skills), html)
        html = re.sub(TEMPLATE_PROJECT_1_TITLE, self.data.projects[0].title, html)
        html = re.sub(TEMPLATE_PROJECT_1_DESCRIPTION, self.data.projects[0].description, html)
        html = re.sub(TEMPLATE_PROJECT_2_TITLE, self.data.projects[1].title, html)
        html = re.sub(TEMPLATE_PROJECT_2_DESCRIPTION, self.data.projects[1].description, html)

        soup = BeautifulSoup(html, 'html.parser')

        # insert the css into the html
        if hasattr(self, 'css'):
            css = soup.new_tag('style')
            css.string = self.css
            soup.head.append(css)

        return soup

    def get_text(self):
        soup = self.get_soup()
        text = ""
        for element in soup.find_all('p'):
            text += element.get_text()

        return text

    def get_html(self):
        soup = self.get_soup()
        return soup.prettify()
    
        

