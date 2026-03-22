# src/pages/inicio.py
from tkinter import Label
from ..utils import Layout

class PaginaInicio(Layout):
    def header(self):
        Label(self, text="🏠 Inicio", font=("Arial", 20, "bold")).pack(pady=20)

    def main(self):
        Label(self, text="Bienvenido a la app").pack()

    def footer(self):
        Label(self, text="v1.0", font=("Arial", 8), foreground="gray").pack(side="bottom", pady=10)