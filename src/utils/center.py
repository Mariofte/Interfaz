from tkinter import Tk

def Center(window:Tk, broad:int, high:int) -> None:
    x = window.winfo_screenwidth()  // 2 - broad // 2
    y = window.winfo_screenheight() // 2 - high // 2
    window.geometry(f"{broad}x{high}+{x}+{y}")