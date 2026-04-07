import os
import json
from typing import Any

class ConfigApp:
    def __init__(self) -> None:
        with open(os.path.join(os.getcwd(), "src", "config", "configs.json"), "r") as f:
            self.__config = json.load(f)
    
    # get all
    def __repr__(self) -> str:
        return f"{self.__config}"
    
    # get one
    def get_attribute(self, key: str) -> Any:
        return self.__config[key]
    
    def get_title(self) -> str:
        return self.get_attribute("title")
    
    def get_broad(self) -> int:
        return self.get_attribute("broad")
    
    def get_height(self) -> int:
        return self.get_attribute("height")
    
    def get_resizable(self) -> list[bool]:
        return self.get_attribute("resizable")
    
    def get_minsize(self) -> list[int]:
        return self.get_attribute("minsize")
    
    def get_maxsize(self) -> list[int]:
        return self.get_attribute("maxsize")