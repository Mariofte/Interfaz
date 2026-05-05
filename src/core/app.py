from tkinter import Tk, Frame
from .router import Router
from ..utils import Center, Logger
from ..views import PaginaConfig, PaginaInicio, PaginaAPIs
from ..views.components import Sidebar

class App(Tk):
    def __init__(self):
        super().__init__()
        self.logger = Logger("App")
        self.logger.info("Iniciando aplicación...")
        self._head()
        self._body()

    def _head(self) -> None:
        self.title("App")
        Center(self, 800, 600)
        self.resizable(
            True,
            True
        )
        self.minsize(
            400,
            300
        )
        self.maxsize(
            1600,
            1200
        )
        self.attributes("-fullscreen", True)
        self.attributes("-fullscreen", False)
        self.attributes("-alpha", 0.9)
        self.attributes("-topmost", True)
        
        self.logger.info("Configuración de ventana establecida.")

    def _body(self) -> None:
        contenedor = Frame(self, bg="white")
        contenedor.pack(side="left", fill="both", expand=True)

        self._router = Router(contenedor)
        self._router.build({
            "Inicio": PaginaInicio,
            "Config": PaginaConfig,
            "APIs": PaginaAPIs
        }) # pyright: ignore[reportArgumentType]

        self._sidebar = Sidebar(self, on_navegar=self._navegar)
        self._sidebar.pack(before=contenedor)

        for nombre in self._router.nombres:
            self._sidebar.add_button(nombre)

        self._navegar("Inicio")

    def _navegar(self, nombre: str) -> None:
        self.logger.info(f"Navegando a {nombre}")
        self._router.navigate(nombre)
        self._sidebar.mark_active(nombre)