import os
import pdfkit
from src.core.coverletter import CoverLetter
from src.core.posting import Posting

from src.core.resume import Resume

def output_to_files(name: str, resume: Resume = None, coverletter: CoverLetter = None, posting: Posting = None, output_dir: str = None):
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
    if not output_dir:
        output_dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../output/"
    
    if not os.path.exists(f"{output_dir}/{name}"):
        os.makedirs(f"{output_dir}/{name}")

    # print the resume to a file
    if resume:
        resume_output_file = f"{output_dir}/{name}/resume.pdf"
        pdfkit.from_string(resume.get_html(), resume_output_file)

    # print the cover letter to a file
    if coverletter:
        coverletter_output_file = f"{output_dir}/{name}/coverletter.txt"
        with open(coverletter_output_file, 'w') as f:
            f.write(coverletter.get_str())

    # print the posting to a file
    if posting:
        posting_output_file = f"{output_dir}/{name}/posting.txt"
        with open(posting_output_file, 'w') as f:
            f.write(posting.get_text())