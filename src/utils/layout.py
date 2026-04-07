from collections.abc import Callable
from tkinter import Misc
from tkinter.ttk import Frame
from abc import ABCMeta, abstractmethod

class _LayoutMeta(ABCMeta, type(Frame)):
    pass

class Layout(Frame, metaclass=_LayoutMeta):
    def __init__(self, master: Misc | None = None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.render()

    def render(self) -> None:
        self.header()
        self.main()
        self.footer()

    @abstractmethod
    def header(self) -> None: pass

    @abstractmethod
    def main(self) -> None: pass

    @abstractmethod
    def footer(self) -> None: pass