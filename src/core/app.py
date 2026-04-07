from tkinter import Tk, Frame
from utils.center import Center
from ..config import ConfigApp
from .router import Router
from ..utils import Center, Logger
from ..views import PaginaConfig, PaginaInicio
from ..views.components import Sidebar

class App(Tk):
    def __init__(self):
        super().__init__()
        self.__config = ConfigApp()
        self._head()
        self._body()

    def _head(self) -> None:
        self.title(self.__config.get_title())
        Center(self, self.__config.get_broad(), self.__config.get_height())
        self.resizable(self.__config.get_resizable()[0], self.__config.get_resizable()[1])
        self.minsize(self.__config.get_minsize()[0], self.__config.get_minsize()[1])
        self.maxsize(self.__config.get_maxsize()[0], self.__config.get_maxsize()[1])
        self.state("zoomed")
        self.attributes("-fullscreen", True)
        self.attributes("-fullscreen", False)
        self.attributes("-alpha", 0.9)
        self.attributes("-topmost", True)

    def _body(self) -> None:
        contenedor = Frame(self, bg="white")
        contenedor.pack(side="left", fill="both", expand=True)

        self._router = Router(contenedor)
        self._router.build({
            "Inicio": PaginaInicio,
            "Config": PaginaConfig,
        }) # pyright: ignore[reportArgumentType]

        self._sidebar = Sidebar(self, on_navegar=self._navegar)
        self._sidebar.pack(before=contenedor)

        for nombre in self._router.nombres:
            self._sidebar.add_button(nombre)

        self._navegar("Inicio")

    def _navegar(self, nombre: str) -> None:
        self._router.navigate(nombre)
        self._sidebar.mark_active(nombre)