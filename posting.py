import re
import numpy as np
import pyperclip as pc


class Posting:
    def __init__(self):
        self.text: str = ""

    def get_text_from_clipboard(self):
        return pc.paste()
    
    def compile(self):
        pass
        
    def get_str(self):
        if hasattr(self, 'text') and self.text:
            return self.text
        self.text = self.get_text_from_clipboard()
        return self.text
        
            