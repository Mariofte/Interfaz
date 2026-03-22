from tkinter import Tk

from ..utils import Center

class App(Tk):
    def __init__(self):
        super().__init__(
            screenName="Hola mundo",
            baseName="Hmoew"
        )
        self.head()
    
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
        pass
        
    def __repr__(self) -> str:
        return super().__repr__()