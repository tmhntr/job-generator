import PySimpleGUI as sg

from src.gui.screen import Screen

# sg.theme('DarkAmber')   # Add a touch of color
class OptionsScreen(Screen):
    def __init__(self, next=None):
        super().__init__(next)

        default_dir = "output/"
        self.layout = [
            [sg.Text('Job (Application) Generator', font='Helvetica 24', justification='center', p=(12, 0))],
            [sg.Text('Options')],
            [sg.Text('Output directory: ', size=(15, 1)), sg.InputText(key='-OUTPUTDIR-',expand_x=True, p=(12, 0), default_text=default_dir)],
            [sg.Text('Options: ', size=(15, 1)), sg.Checkbox('Generate cover letter', key='-COVERLETTER-', default=True), sg.Checkbox('Generate resume', key='-RESUME-', default=True), sg.Checkbox('Generate posting', key='-POSTING-', default=True)],
            [sg.Button('Generate', expand_x=True, expand_y=True, p=(48, 64))]
        ]

    def update(self, event, values, window):
        if event == 'Generate':
            window.write_event_value('-GENERATE-', None)
            window.write_event_value('-NEXT-', None)
        

