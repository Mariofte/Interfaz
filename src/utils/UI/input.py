from tkinter import Frame, Entry, Label, Misc

class Input(Frame):
    def __init__(self, label:str, placeholder:str, **kwargs):
        super().__init__(self, **kwargs)
        self.__label:Label = Label(self, text=label)
        self.__entry:Entry = Entry(self)