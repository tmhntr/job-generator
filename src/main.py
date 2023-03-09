#!/Applications/anaconda3/envs/resume/bin/python
import os
from argparse import ArgumentParser
from src.gui.gui import App

from src.core.coverletter import CoverLetter
from src.core.data import DataFactory
from src.core.posting import Posting
from src.core.resume import Resume
from src.core.utils import output_to_files

from src.constants import resume_template_html, resume_template_css

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
    parser.add_argument("-d", "--dir", dest="output_dir", default=f"{os.path.dirname(os.path.abspath(__file__))}/../output/")

    args = parser.parse_args()
    return args



def main():
    args = my_parse_args()
    
    data_file = f"{os.path.dirname(os.path.abspath(__file__))}/../data/data.json"
 
    if args.no_gui:
        posting = Posting()
        factory = DataFactory(data_file=data_file)
        name = posting.get_name_from_input()
        posting.get_text_from_input()

        resume_data = factory.get_resume_data(posting=posting.get_text())
        resume = Resume(html_template_file=resume_template_html, data=resume_data, css_file=resume_template_css)

        coverletter = CoverLetter(resume.get_text(), posting.get_text())

    else:
        app = App(data_file=data_file)
        app.run()
        posting = app.posting
        name = app.posting.get_name()
        resume = app.resume
        coverletter = app.coverletter


    if args.output:
        output_to_files(
            name=name,
            resume=resume if args.resume else None, 
            coverletter=coverletter if args.letter else None, 
            posting=posting if args.posting else None, 
            output_dir=args.output_dir)
        
    if args.verbose:
        if args.resume:
            print(resume.get_html())
        if args.letter:
            print(coverletter.get_str())
        if args.posting:
            print(posting.get_text())


if __name__ == '__main__':
    main()

