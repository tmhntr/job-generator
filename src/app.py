#!/Applications/anaconda3/envs/resume/bin/python
import os
from argparse import ArgumentParser
from src.cli import CLI
from src.gui.gui import App

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
    parser.add_argument("-d", "--dir", dest="output_dir", default=f"{os.path.dirname(os.path.abspath(__file__))}/../output/")

    args = parser.parse_args()
    return args



def main():
    
    data_file = f"{os.path.dirname(os.path.abspath(__file__))}/../data/data.json"
 
    args = my_parse_args()

    if args.no_gui:
        app = CLI(data_file=data_file)
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

