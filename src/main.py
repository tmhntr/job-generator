#!/Applications/anaconda3/envs/resume/bin/python
import pdfkit
import os
from argparse import ArgumentParser

from src.core.coverletter import CoverLetter
from src.core.data import DataFactory
from src.core.posting import Posting
from src.core.resume import Resume
from src.core.utils import output_to_files

def my_parse_args():
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", dest="verbose", action="store_true",
                        help="verbose output")
    parser.add_argument("--no-gui", dest="no_gui", action="store_true",
                        help="no gui")
    parser.add_argument("-r", "--resume", action='store_true')
    parser.add_argument("-l", "--letter", action='store_true')
    parser.add_argument("-o", "--output", action='store_true')
    parser.add_argument("-p", "--posting", action='store_true')
    parser.add_argument("-d", "--data", dest="data", default=f"{os.path.dirname(os.path.abspath(__file__))}/../data/data.json")

    args = parser.parse_args()
    return args



def default_file_names(name: str):
    """Returns the default file names for the resume, cover letter, and posting.
    
    Args:
        name (str): The name of the company.
    
    Returns:
        tuple: The default file names for the resume, cover letter, and posting.
        """
    resume_output_file = f"{os.path.dirname(os.path.abspath(__file__))}/../output/{name}/Resume.pdf"
    coverletter_output_file = f"{os.path.dirname(os.path.abspath(__file__))}/../output/{name}/CoverLetter.txt"
    posting_output_file = f"{os.path.dirname(os.path.abspath(__file__))}/../output/{name}/Posting.txt"
    return resume_output_file, coverletter_output_file, posting_output_file

def template_file_names():
    """Returns the default file names for the resume, cover letter, and posting.
    
    Args:
        name (str): The name of the company.
    
    Returns:
        tuple: The default file names for the resume, cover letter, and posting.
        """
    resume_template_html = f"{os.path.dirname(os.path.abspath(__file__))}/../templates/resume.html"
    resume_template_css = f"{os.path.dirname(os.path.abspath(__file__))}/../templates/style.css"
    return resume_template_html, resume_template_css

def main():
    args = my_parse_args()
    
    if not os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}/../output/{args.name}"):
        os.makedirs(f"{os.path.dirname(os.path.abspath(__file__))}/../output/{args.name}")
        
    resume_output_file, coverletter_output_file, posting_output_file = default_file_names(args.name)

    resume_template_html, resume_template_css = template_file_names()
    data_file = args.data


    posting = Posting()

    factory = DataFactory(data_file=data_file)
    resume_data = factory.get_resume_data(posting=posting.get_str())

    resume = Resume(html_template_file=resume_template_html, data=resume_data, css_file=resume_template_css)
    coverletter = CoverLetter(resume.get_text(), posting.get_str())

    if args.output:
        output_to_files(
            resume=resume if args.resume else None, 
            coverletter=coverletter if args.letter else None, 
            posting=posting if args.posting else None, 
            resume_output_file=resume_output_file, 
            coverletter_output_file=coverletter_output_file, 
            posting_output_file=posting_output_file)
        
    if args.verbose:
        if args.resume:
            print(resume.get_html())
        if args.letter:
            print(coverletter.get_str())
        if args.posting:
            print(posting.get_str())


if __name__ == '__main__':
    main()

