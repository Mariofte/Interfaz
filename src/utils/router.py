from tkinter import Frame, Misc
from typing import Type

class Router:
    def __init__(self, container: Misc) -> None:
        self._container = container
        self._paginas: dict[str, Frame] = {}
    
    def register(self, name:str, page_class: Type[Frame]) -> None:
        page = page_class(self._container)
        page.place(relheight=1, relwidth=1)
        self._paginas[name] = page
    
    def navigate(self, name: str) -> None:
        self._paginas[name].tkraise()
    
    @property
    def nombres(self) -> list[str]:
        return list(self._paginas.keys())