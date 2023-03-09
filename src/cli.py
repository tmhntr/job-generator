from src.core.coverletter import CoverLetter
from src.core.posting import Posting
from src.core.resume import Resume
from src.constants import resume_template_html, resume_template_css


class CLI:
    def __init__(self, data_file: str):
        self.posting = Posting()
        self.data_file = data_file

    def run(self):
        self.name = self.posting.get_name_from_input()
        self.posting.get_text_from_input()

        self.resume = Resume(data_file=self.data_file, posting_text=self.posting.get_text(), html_template_file=resume_template_html, css_file=resume_template_css)

        self.coverletter = CoverLetter(self.resume.get_text(), self.posting.get_text())