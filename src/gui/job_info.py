import PySimpleGUI as sg
from src.core.posting import Posting

from src.gui.screen import Screen

# sg.theme('DarkAmber')   # Add a touch of color
class JobInfoScreen(Screen):
    def __init__(self, posting: Posting, next=None):
        super().__init__(next)
        self.posting = posting
        self.layout = [
            [sg.Text('Job (Application) Generator', font='Helvetica 24', justification='center', p=(12, 0))],
            [sg.Text('Job Info')],
            [sg.Text('Job/Company Name', size=(15, 1))],
            [sg.InputText(key='-POSTINGNAME-',expand_x=True, p=(12, 0))],
            [sg.Text('Job listing text', size=(15, 1))],
            [sg.InputText(key='-POSTINGTEXT-',expand_x=True, expand_y=True, p=(12, 0))],
            [sg.Button('Next', expand_x=True, p=(48, 64, 0, 0))]
        ]

    def update(self, event, values, window):
        if event == 'Next':
            window.write_event_value('-POSTING-', values)
            window.write_event_value('-NEXT-', None)
        

