from src.core.coverletter import CoverLetter
from src.core.posting import Posting
from src.core.resume import Resume
from src.constants import resume_template_html, resume_template_css


class CLI:
    def __init__(self, data_file: str, posting: Posting = None, data_factory: DataFactory = None):
        self.posting = posting if posting else Posting()
        self.factory = data_factory if data_factory else DataFactory(data_file=data_file)

    def run(self):
        self.name = self.posting.get_name_from_input()
        self.posting.get_text_from_input()

        resume_data = self.factory.get_resume_data(posting=self.posting.get_text())
        resume = Resume(html_template_file=resume_template_html, data=resume_data, css_file=resume_template_css)

        self.coverletter = CoverLetter(resume.get_text(), self.posting.get_text())