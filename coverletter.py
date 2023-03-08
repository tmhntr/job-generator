from chatgpt import Bot

prompt = """
I'm about to send you a resume and then a job listing. 
You will write a cover letter based on the resume and job listing, emphasizing skills from the resume.
It should be 3 paragraphs long. Use the name Tim Hunter as the applicant.
"""

class CoverLetter:
    def __init__(self, resume_str: str, posting_str: str):
        self.bot: Bot = Bot()

        self.resume_str = resume_str
        self.posting_str = posting_str

        self.cover_letter_str: str = ""

    def request_coverletter(self) -> str:
        self.bot.messages = []
        self.bot.new_message('user', prompt)
        self.bot.new_message('user', self.resume_str)
        self.bot.new_message('user', self.posting_str)

        return self.bot.get_response()
        

    def get_str(self):
        if self.cover_letter_str == "":
            self.cover_letter_str = self.request_coverletter()
        
        return self.cover_letter_str

        


