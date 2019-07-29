from tkinter import Tk


class Label(Tk):
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t
        self.create_label()

    def create_label(self):
        self.label = Label(text=str(self.t), padx=self.x, pady=self.y)

    def change_text(self, text):
        self.label.config(text=str(text))
