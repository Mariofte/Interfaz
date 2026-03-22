# src/pages/config.py
from tkinter import Label
from ..utils import Layout

class PaginaConfig(Layout):
    def header(self):
        Label(self, text="⚙️ Configuración", font=("Arial", 20, "bold")).pack(pady=20)

    def main(self):
        Label(self, text="Aquí van las opciones").pack()

    def footer(self):
        Label(self, text="Config", font=("Arial", 8), foreground="gray").pack(side="bottom", pady=10)