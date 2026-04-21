from tkinter import Label, Entry, Frame
from ..utils import Layout

from ..Lib import ScannerAPI

class PaginaAPIs(Layout):
    def header(self):
        Label(self, text="🔌 APIs", font=("Arial", 20, "bold")).pack(pady=20)
    
    def main(self):
        pass

    def footer(self):
        Label(self, text="APIs", font=("Arial", 8), foreground="gray").pack(side="bottom", pady=10)