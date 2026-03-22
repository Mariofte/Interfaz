from collections.abc import Callable
from tkinter import Misc
from tkinter.ttk import Frame
from abc import ABCMeta, abstractmethod
from typing import Literal
from types import EllipsisType

# Combina ABCMeta con la metaclass de Frame
class _LayoutMeta(ABCMeta, type(Frame)):
    pass


class Layout(Frame, metaclass=_LayoutMeta):
    def __init__(self, master: Misc | None = None, *, border: float | str = ..., borderwidth: float | str = ..., class_: str = "", cursor: str | tuple[str] | tuple[str, str] | tuple[str, str, str] | tuple[str, str, str, str] = "", height: float | str = 0, name: str = ..., padding: float | str | tuple[float | str] | tuple[float | str, float | str] | tuple[float | str, float | str, float | str] | tuple[float | str, float | str, float | str, float | str] = ..., relief: Literal['raised'] | Literal['sunken'] | Literal['flat'] | Literal['ridge'] | Literal['solid'] | Literal['groove'] = ..., style: str = "", takefocus: bool | Callable[[str], bool | None] | Literal[0] | Literal[1] | Literal[''] = "", width: float | str = 0) -> None: # pyright: ignore[reportArgumentType]
        super().__init__(master, border=border, borderwidth=borderwidth, class_=class_, cursor=cursor, height=height, name=name, padding=padding, relief=relief, style=style, takefocus=takefocus, width=width) # type: ignore[arg-type]

        
    def render(self) -> None:
        self.header()
        self.main()
        self.footer()
    
    @abstractmethod
    def header(self) -> None:
        pass
    
    @abstractmethod
    def main(self) -> None:
        pass
    
    @abstractmethod
    def footer(self) -> None:
        pass