import pyperclip as pc


class Posting:
    def __init__(self):
        self.name: str = ""
        self.text: str = ""

    def get_text_from_clipboard(self):
        return pc.paste()
    
    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def compile(self):
        pass
        
    def get_str(self):
        if hasattr(self, 'text') and self.text:
            return self.text
        self.text = self.get_text_from_clipboard()
        return self.text
        
            