import json
import PySimpleGUI as sg
from collections import deque
from src.core.coverletter import CoverLetter

from src.core.resume import Resume, ResumeData
from src.constants import resume_template_html, resume_template_css
from src.core.utils import output_to_files

from src.gui.applicant_info import ApplicantInfoScreen
from src.gui.job_info import JobInfoScreen
from src.gui.options import OptionsScreen
from src.gui.home import HomeScreen

from src.core.posting import Posting
from src.gui.screen import Screen


sg.set_options(font=('Arial Black', 14))
# set the size of the window, and make it resizable
sg.set_options(button_element_size=(12, 1), element_padding=(8, 12))
# All the stuff inside your window.

class ErrorPopup:
    def __init__(self, error_message: str):
        layout = [  [sg.Text('ERROR', justification='center')],
                    [sg.Text(error_message, justification='center')],
                    [sg.Button('Ok')] ]

        # Create the Window
        window = sg.Window('Window Title', layout)
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Ok': # if user closes window or clicks cancel
                break

        window.close()


class App:
    screen_dq = deque(['Home', 'JobInfo', 'ApplicantInfo', 'Options'])
    window = None

    def __init__(self, data_file: str, posting: Posting = None):
        self.posting = posting if posting else Posting()

        self.data_file =data_file

        self.window_title = 'Job (Application) Generator'
        self.set_screen(HomeScreen())
        
    
    def set_screen(self, screen: Screen):
        self.screen = screen
        self.state = screen.screen_name
        if hasattr(self, 'window') and self.window:
            self.window.close()
        self.window = sg.Window(self.window_title, self.screen.layout, size=(700, 500))


    def handle_home_event(self, event, values):
        if event == '-NEXT-':
            self.set_screen(JobInfoScreen(self.posting))

    def handle_job_info_event(self, event, values):
        if event == '-NEXT-':
            self.posting.set_name(values['-POSTINGNAME-'])
            self.posting.set_text(values['-POSTINGTEXT-'])
            if not hasattr(self, 'resume_data'):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.resume_data = ResumeData(**data['resume'])
            self.set_screen(ApplicantInfoScreen(self.resume_data))

    def handle_applicant_info_event(self, event, values):
        if event == '-NEXT-':
            if not hasattr(self, 'resume_data'):
                self.resume_data = ResumeData()
            self.resume_data.name = values['-NAME-']
            self.resume_data.email = values['-EMAIL-']
            self.resume_data.address = values['-ADDRESS-']
            self.resume_data.website = values['-WEBSITE-']
            self.resume_data.skills = values['-SKILLS-'].split(', ')
            self.set_screen(OptionsScreen())
    
    def handle_options_event(self, event, values):
        if event == '-GENERATE-':
            if not hasattr(self, 'resume_data'):
                raise Exception('Resume data not set')


            self.resume = Resume(data_file=self.data_file, html_template_file=resume_template_html, css_file=resume_template_css, posting_text=self.posting.get_text())
            self.cover_letter = CoverLetter(resume_str=self.resume.get_text(), posting_str=self.posting.get_text())
            output_to_files(
                name=self.posting.get_name(),
                resume=self.resume if values['-RESUME-'] else None, 
                coverletter=self.cover_letter if values['-COVERLETTER-'] else None,
                posting=self.posting if values['-POSTING-'] else None, 
                output_dir=values['-OUTPUTDIR-'])
            self.set_screen(HomeScreen())

    def handle_event(self, event, values):
        self.state_event_map[self.state](event, values)


    def run(self):
        state_event_map = {
            'Home': self.handle_home_event,
            'JobInfo': self.handle_job_info_event,
            'ApplicantInfo': self.handle_applicant_info_event,
            'Options': self.handle_options_event
        }

        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break

            try:
                state_event_map[self.state](event, values)
                self.screen.update(event, values, self.window)
            except Exception as e:
                ErrorPopup(error_message=str(e))

        self.window.close()


# Create the Window
if __name__ == '__main__':
    app = App(data_file='data/data.json')
    app.run()