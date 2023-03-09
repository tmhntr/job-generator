import pyperclip as pc


class Posting:
    def __init__(self):
        self.name = None
        self.text = None

    def get_text_from_clipboard(self):
        return pc.paste()
    
    def set_text(self, text: str):
        self.text = text

    # def get_text(self):
    #     return self.text
    
    def get_name(self):
        if self.name is None:
            raise Exception("Posting name is not set")
        return self.name
    
    def set_name(self, name: str):
        self.name = name
    
    def get_text_from_clipboard(self):
        self.text = pc.paste()
        return self.text
    
    def get_name_from_input(self):
        self.name = input("Enter the company/job name: ")
        return self.name

    def get_text_from_input(self):
        self.text = input("Enter the posting text: ")
        return self.text
        
    def get_text(self):
        if self.text is None:
            raise Exception("Posting text is not set")
        return self.text
        
            