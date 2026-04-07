from tkinter import Tk

def Center(window:Tk, broad:int, height:int) -> None:
    x = window.winfo_screenwidth()  // 2 - broad // 2
    y = window.winfo_screenheight() // 2 - height // 2
    window.geometry(f"{broad}x{height}+{x}+{y}")