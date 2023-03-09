import PySimpleGUI as sg

from src.gui.screen import Screen

# sg.theme('DarkAmber')   # Add a touch of color
class HomeScreen(Screen):
    screen_name = 'Home'
    def __init__(self):
        self.layout = [
            [sg.Text('Job (Application) Generator', font='Helvetica 24', justification='center', p=(12, 0))],
            [sg.Text('Home')],
            [sg.Button('Start', size=(12, 1))]
        ]

    def update(self, event, values, window):
        if event == 'Start':
            window.write_event_value('-NEXT-', values)
        

