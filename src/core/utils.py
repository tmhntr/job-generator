import os
import pdfkit
from src.core.coverletter import CoverLetter
from src.core.posting import Posting

from src.core.resume import Resume

def output_to_files(resume: Resume = None, coverletter: CoverLetter = None, posting: Posting = None, resume_output_file: str = None, coverletter_output_file: str = None, posting_output_file: str = None):
    """Print the resume, cover letter, and posting to files.
    Each one is passed as an optional argument.
    
    Args:
        resume (Resume, optional): The resume to print. Defaults to None.
        coverletter (CoverLetter, optional): The cover letter to print. Defaults to None.
        posting (Posting, optional): The posting to print. Defaults to None.
        resume_output_file (str, optional): The file to print the resume to. Defaults to output/Resume.pdf.
        coverletter_output_file (str, optional): The file to print the cover letter to. Defaults to output/CoverLetter.txt.
        posting_output_file (str, optional): The file to print the posting to. Defaults to output/Posting.txt.
        """

    # print the resume to a file
    if resume:
        if not resume_output_file:
            resume_output_file = f"{os.path.dirname(os.path.abspath(__file__))}/../output/Resume.pdf"
        pdfkit.from_string(resume.get_html(), resume_output_file)

    # print the cover letter to a file
    if coverletter:
        if not coverletter_output_file:
            coverletter_output_file = f"{os.path.dirname(os.path.abspath(__file__))}/../output/CoverLetter.txt"
        with open(coverletter_output_file, 'w') as f:
            f.write(coverletter.get_str())

    # print the posting to a file
    if posting:
        if not posting_output_file:
            posting_output_file = f"{os.path.dirname(os.path.abspath(__file__))}/../output/Posting.txt"
        with open(posting_output_file, 'w') as f:
            f.write(posting.get_str())