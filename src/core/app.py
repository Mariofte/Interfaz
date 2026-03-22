from tkinter import Frame, Tk

from .sidebar import Sidebar

from ..utils import Center, Router

from ..views import PaginaConfig, PaginaInicio

class App(Tk):
    def __init__(self):
        super().__init__(
            screenName="Hola mundo",
            baseName="Hmoew"
        )
        self.head()
        self.body()
    
    def head(self) -> None:
        # ====================
        # Groove             |
        # ====================
        self.title("Mi App")
        
        # ====================
        # Geometry           |
        # ====================
        Center(self, 800, 600)
        self.resizable(True, True)
        self.minsize(500, 500)
        self.maxsize(1280, 720)
        
        # ====================
        # Screen features    |
        # ====================
        self.state("zoomed")
        self.attributes("-fullscreen", True)
        self.attributes("-fullscreen", False)
        self.attributes("-alpha", 0.9)
        self.attributes("-topmost", True)
    
    def body(self) -> None:
# 1. Área de contenido (va a la derecha)
        contenedor = Frame(self, bg="white")
        contenedor.pack(side="left", fill="both", expand=True)

        # 2. Router — registra las páginas
        self.router = Router(contenedor)
        self.router.register("Inicio",  Frame)   # ← reemplaza Frame con tus páginas reales
        self.router.register("Config",  Frame)

        # 3. Sidebar — conectada al router
        self.sidebar = Sidebar(self, on_navegar=self._navegar)
        self.sidebar.pack(before=contenedor)

        for nombre in self.router.nombres:
            self.sidebar.add_button(nombre)

        self._navegar("Inicio")  # página inicial

    def _navegar(self, nombre: str) -> None:
        self.router.navigate(nombre)
        self.sidebar.mark_active(nombre)
        
    def __repr__(self) -> str:
        return super().__repr__()