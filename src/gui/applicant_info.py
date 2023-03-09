import PySimpleGUI as sg
from src.core.resume import ResumeData

from src.gui.screen import Screen

# sg.theme('DarkAmber')   # Add a touch of color
class ApplicantInfoScreen(Screen):
    screen_name = 'ApplicantInfo'
    def __init__(self, resume_data: ResumeData):
        self.resume_data = resume_data
        self.layout = [
            [sg.Text('Job (Application) Generator', font='Helvetica 24', justification='center', p=(12, 0))],
            [sg.Text('Applicant Info')],
            [sg.Text('Name', size=(15, 1)), sg.InputText(key='-NAME-',expand_x=True, p=(12, 0), default_text=self.resume_data.name)],
            [sg.Text('Email', size=(15, 1)), sg.InputText(key='-EMAIL-',expand_x=True, p=(12, 0), default_text=self.resume_data.email)],
            [sg.Text('Address', size=(15, 1)), sg.InputText(key='-ADDRESS-',expand_x=True, p=(12, 0), default_text=self.resume_data.address)],
            [sg.Text('Website', size=(15, 1)), sg.InputText(key='-WEBSITE-',expand_x=True, p=(12, 0), default_text=self.resume_data.website)],
            [sg.Text('Skills', size=(15, 1)), sg.InputText(key='-SKILLS-',expand_x=True, p=(12, 0), default_text=", ".join(self.resume_data.skills))],
            [sg.Button('Next', expand_x=True, p=(48, 64, 0, 0))]
        ]

    def update(self, event, values, window):
        if event == 'Next':
            window.write_event_value('-DATA-', values)
            window.write_event_value('-NEXT-', None)
        

