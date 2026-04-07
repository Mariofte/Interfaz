from tkinter import Button, Frame, Misc
from typing import Callable

class Sidebar(Frame):
    def __init__(self, parent: Misc, on_navegar: Callable[[str], None]) -> None:
        super().__init__(parent, bg="#0E0EC3", width=160)
        self.pack(side="left", fill="y")
        self.pack_propagate(False)
        self._on_navegar = on_navegar
        self._btns: dict[str, Button] = {}
    
    def add_button(self, nombre: str) -> None:
        btn = Button(self,
                        text=nombre,
                        font=("Arial", 11),
                        bg="#1A1A2E", fg="#888888",
                        activebackground="#0F3460",
                        activeforeground="white",
                        relief="flat", cursor="hand2",
                        anchor="w", padx=20, pady=12,
                        command=lambda n=nombre: self._on_navegar(n))
        btn.pack(fill="x")
        self._btns[nombre] = btn
    
    def mark_active(self, nombre) -> None:
        for b in self._btns.values():
            b.config(bg="#1A1A2E", fg="#888888")
        self._btns[nombre].config(bg="#0F3460", fg="white")