from bs4 import BeautifulSoup
import re

from data import ResumeData


TEMPLATE_SKILLS = "TEMPLATE_SKILLS"
TEMPLATE_PROJECT_1_TITLE = "TEMPLATE_PROJECT_1_TITLE"
TEMPLATE_PROJECT_1_DESCRIPTION = "TEMPLATE_PROJECT_1_DESCRIPTION"
TEMPLATE_PROJECT_2_TITLE = "TEMPLATE_PROJECT_2_TITLE"
TEMPLATE_PROJECT_2_DESCRIPTION = "TEMPLATE_PROJECT_2_DESCRIPTION"


class Resume:
    skills_limit: int = 6

    def __init__(self, html_template_file: str, data: ResumeData, css_file: str = ""):
        self.data: ResumeData = data

        # read the html file to a variable
        with open(html_template_file, 'r') as f:
            html = f.readlines()
            
        self.html_template = "".join(html)

        if css_file:
            with open(css_file, 'r') as f:
                self.css = "".join(f.readlines())

        self.soup = self.compile_soup()

    def skill_string(self, skills: list[str]):
        s = ""
        for skill in skills:
            s += f"{skill}, "
        s = s[0].upper() + s[1:-2] + "."
        return s

    def compile_soup(self):
        html = self.html_template
        html = re.sub(TEMPLATE_SKILLS, self.skill_string(self.data.skills), html)
        html = re.sub(TEMPLATE_PROJECT_1_TITLE, self.data.projects[0].title, html)
        html = re.sub(TEMPLATE_PROJECT_1_DESCRIPTION, self.data.projects[0].description, html)
        html = re.sub(TEMPLATE_PROJECT_2_TITLE, self.data.projects[1].title, html)
        html = re.sub(TEMPLATE_PROJECT_2_DESCRIPTION, self.data.projects[1].description, html)

        soup = BeautifulSoup(html, 'html.parser')

        # insert the css into the html
        if self.css:
            css = soup.new_tag('style')
            css.string = self.css
            soup.head.append(css)

        return soup

    def get_text(self):
        text = ""
        for element in self.soup.find_all('p'):
            text += element.get_text()

        return text

    def get_html(self):
        return self.soup.prettify()
    
        

