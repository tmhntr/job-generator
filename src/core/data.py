import json

from dataclasses import dataclass
import re
from typing import Union

import numpy as np

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
    name: str
    email: str
    website: str
    address: str
    projects: list[ProjectData]
    posting: str
    skills_data: SkillsData

    def __post_init__(self):
        self.skills = self.skills_data.get_skills(self.posting, limit=6)


class DataFactory:
    def __init__(self, data_file: str):
        self.data_file = data_file

    def get_resume_data(self, posting: str) -> ResumeData:
        skills_data = self.get_skills_data()
        with open(self.data_file, 'r') as f:
            data = json.load(f)
        projects = [ProjectData(**project) for project in data['projects']]
        return ResumeData(skills_data=skills_data, projects=projects, posting=posting, **data['resume'])
    
    
    def get_skills_data(self) -> SkillsData:
        with open(self.data_file, 'r') as f:
            data = json.load(f)
        return SkillsData(data['skills_relatedness'])