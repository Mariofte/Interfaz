import tkinter as tk


# ══════════════════════════════════════════════════════
#  SIDEBAR — solo maneja la barra lateral
# ══════════════════════════════════════════════════════
class Sidebar(tk.Frame):
    def __init__(self, parent, on_navegar):
        super().__init__(parent, bg="#1A1A2E", width=160)
        self.pack(side="left", fill="y")
        self.pack_propagate(False)
        self._on_navegar = on_navegar  # callback al hacer clic
        self._btns = {}

    def agregar_boton(self, nombre):
        btn = tk.Button(self,
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

    def marcar_activo(self, nombre):
        for b in self._btns.values():
            b.config(bg="#1A1A2E", fg="#888888")
        self._btns[nombre].config(bg="#0F3460", fg="white")


# ══════════════════════════════════════════════════════
#  ROUTER — maneja las páginas y la navegación
# ══════════════════════════════════════════════════════
class Router:
    def __init__(self, contenedor):
        self._contenedor = contenedor
        self._paginas = {}

    def registrar(self, nombre, clase):
        pagina = clase(self._contenedor)
        pagina.place(relwidth=1, relheight=1)
        self._paginas[nombre] = pagina

    def navegar(self, nombre):
        self._paginas[nombre].tkraise()

    @property
    def nombres(self):
        return list(self._paginas.keys())


# ══════════════════════════════════════════════════════
#  APP — solo conecta las piezas
# ══════════════════════════════════════════════════════
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mi App")
        self.geometry("600x400")

        # Área de contenido
        contenedor = tk.Frame(self, bg="white")
        contenedor.pack(side="left", fill="both", expand=True)

        # Router — registra las páginas
        self.router = Router(contenedor)
        self.router.registrar("Inicio",  PaginaInicio)
        self.router.registrar("Escaneo", PaginaEscaneo)
        self.router.registrar("Config",  PaginaConfig)

        # Sidebar — conectada al router
        self.sidebar = Sidebar(self, on_navegar=self._navegar)
        self.sidebar.pack(before=contenedor)  # va a la izquierda

        for nombre in self.router.nombres:
            self.sidebar.agregar_boton(nombre)

        self._navegar("Inicio")

    def _navegar(self, nombre):
        self.router.navegar(nombre)
        self.sidebar.marcar_activo(nombre)


# ══════════════════════════════════════════════════════
#  PÁGINAS — cada una en su propia clase
# ══════════════════════════════════════════════════════
class PaginaBase(tk.Frame):
    """Clase base — todas las páginas heredan de aquí."""
    def __init__(self, parent, bg="white"):
        super().__init__(parent, bg=bg)

class PaginaInicio(PaginaBase):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Inicio", font=("Arial", 18), bg="white").pack(pady=80)

class PaginaEscaneo(PaginaBase):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Escaneo", font=("Arial", 18), bg="white").pack(pady=80)

class PaginaConfig(PaginaBase):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Config", font=("Arial", 18), bg="white").pack(pady=80)


App().mainloop()