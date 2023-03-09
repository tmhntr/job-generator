import PySimpleGUI as sg
from collections import deque
from src.core.coverletter import CoverLetter

from src.core.data import DataFactory, ResumeData
from src.core.resume import Resume
from src.constants import resume_template_html, resume_template_css
from src.core.utils import output_to_files

from src.gui.applicant_info import ApplicantInfoScreen
from src.gui.job_info import JobInfoScreen
from src.gui.options import OptionsScreen
from src.gui.home import HomeScreen

from src.core.posting import Posting


sg.set_options(font=('Arial Black', 14))
# set the size of the window, and make it resizable
sg.set_options(button_element_size=(12, 1), element_padding=(8, 12))
# All the stuff inside your window.


class ScreenFactory:
    def __init__(self, posting: Posting):
        self.posting = posting
        self.resume_data = DataFactory("data/data.json").get_resume_data(posting=posting.get_text())
        
    def set_resume_data(self, resume_data: ResumeData):
        self.resume_data = resume_data

    def create(self, screen_name: str):
        if screen_name == 'Home':
            return HomeScreen()
        elif screen_name == 'JobInfo':
            return JobInfoScreen(self.posting)
        elif screen_name == 'ApplicantInfo':
            return ApplicantInfoScreen(self.resume_data)
        elif screen_name == 'Options':
            return OptionsScreen()

class App:
    screens = deque(['Home', 'JobInfo', 'ApplicantInfo', 'Options'])

    def __init__(self):
        self.posting = Posting()
        self.window_title = 'Job (Application) Generator'
        self.screen_factory = ScreenFactory(posting=self.posting)
        self.current_screen = self.screen_factory.create(self.current_screen_name)
        self.window = sg.Window(self.window_title, self.current_screen.layout, size=(700, 500))

    @property
    def current_screen_name(self):
        return self.screens[0]
    
    def next(self):
        print('closing window')
        self.window.close()
        self.screens.rotate(-1)
        self.current_screen = self.screen_factory.create(self.current_screen_name)

        self.window = sg.Window(self.window_title, self.current_screen.layout, size=(700, 500))

    def handle_event(self, event, values):
        if event == "-POSTING-":
            self.posting.set_text(values['-POSTINGTEXT-'])
            self.posting.set_name(values['-POSTINGNAME-'])
            self.resume_data = DataFactory("data/data.json").get_resume_data(posting=self.posting.get_text())
            self.screen_factory.set_resume_data(self.resume_data)

        if event == "-DATA-":
            if self.resume_data:
                self.resume_data.address = values['-ADDRESS-']
                self.resume_data.email = values['-EMAIL-']
                self.resume_data.website = values['-WEBSITE-']
                self.resume_data.name = values['-NAME-']
                self.resume_data.skills = values['-SKILLS-'].split(', ')

        if event == "-GENERATE-":

            resume = Resume(html_template_file=resume_template_html, css_file=resume_template_css, data=self.resume_data)
            cover_letter = CoverLetter(resume.get_text(), self.posting.get_text())
            args = {}
            if values['-RESUME-']:
                args['resume'] = resume
                args['resume_output_file'] = values['-OUTPUTDIR-']+ "/" + self.posting.get_name().title().replace(" ", "") + 'Resume.pdf'

            if values['-COVERLETTER-']:
                args['coverletter'] = cover_letter
                args['coverletter_output_file'] = values['-OUTPUTDIR-'] + "/" + self.posting.get_name().title().replace(" ", "") + 'CoverLetter.txt'

            if values['-POSTING-']:
                args['posting'] = self.posting
                args['posting_output_file'] = values['-OUTPUTDIR-'] + "/" + self.posting.get_name().title().replace(" ", "") + 'Posting.txt'

            output_to_files(**args)
            

        if event == "-NEXT-":
            self.next()


    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break

            self.current_screen.update(event, values, self.window)

            self.handle_event(event, values)

        self.window.close()


# Create the Window
# Event Loop to process "events" and get the "values" of the inputs


app = App()
app.run()