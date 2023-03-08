#!/Applications/anaconda3/envs/resume/bin/python
import pdfkit
import os
from argparse import ArgumentParser

from coverletter import CoverLetter
from data import DataFactory
from posting import Posting
from resume import Resume

def my_parse_args():
    parser = ArgumentParser()
    parser.add_argument("name", help="company name", default="new", nargs="?")
    parser.add_argument("-v", "--verbose", dest="verbose", action="store_true",
                        help="verbose output")
    parser.add_argument("-r", "--resume", action='store_true')
    parser.add_argument("-l", "--letter", action='store_true')
    parser.add_argument("-o", "--output", action='store_true')
    parser.add_argument("-p", "--posting", action='store_true')
    parser.add_argument("-d", "--data", dest="data", default=f"{os.path.dirname(os.path.abspath(__file__))}/data/data.json")

    args = parser.parse_args()
    return args

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    args = my_parse_args()
    
    if not os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}/output/{args.name}"):
        os.makedirs(f"{os.path.dirname(os.path.abspath(__file__))}/output/{args.name}")
        
    resume_output_file = f"{os.path.dirname(os.path.abspath(__file__))}/output/{args.name}/Resume.pdf"
    coverletter_output_file = f"{os.path.dirname(os.path.abspath(__file__))}/output/{args.name}/CoverLetter.txt"
    posting_output_file = f"{os.path.dirname(os.path.abspath(__file__))}/output/{args.name}/Posting.txt"

    resume_template = f"{os.path.dirname(os.path.abspath(__file__))}/templates/resume.html"
    css_file = f"{os.path.dirname(os.path.abspath(__file__))}/templates/style.css"
    data_file = args.data

    posting = Posting()

    factory = DataFactory(data_file=data_file)
    resume_data = factory.get_resume_data(posting=posting.get_str())

    resume = Resume(html_template_file=resume_template, data=resume_data, css_file=css_file)
    coverletter = CoverLetter(resume.get_text(), posting.get_str())

    if args.output:
        if args.resume:
            pdfkit.from_string(resume.get_html(), resume_output_file)
        if args.letter:
            with open(coverletter_output_file, 'w') as f:
                f.write(coverletter.get_str())
            # pdfkit.from_string(coverletter_str, coverletter_output_file)
        if args.posting:
            with open(posting_output_file, 'w') as f:
                f.write(posting.get_str())

    if args.verbose:
        if args.resume:
            print(resume.get_html())
        if args.letter:
            print(coverletter.get_str())
        if args.posting:
            print(posting.get_str())


if __name__ == '__main__':
    main()
