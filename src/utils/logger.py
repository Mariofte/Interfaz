import os
import logging as log
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, name:str, level=log.DEBUG, archive: str | None = None):
        self.logger = log.getLogger(name)
        self.logger.setLevel(level)
        
        if not self.logger.handlers:
            formatter = log.Formatter(
                '  %(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            """
            console = log.StreamHandler()
            console.setLevel(level)
            console.setFormatter(formatter)
            self.logger.addHandler(console)
            """
            
            if archive:
                formatter = log.Formatter(
                    '  %(asctime)s  [%(name)s]  {%(levelname)s} | %(message)s'
                )
                file = RotatingFileHandler(
                    filename=archive,
                    maxBytes=1_000_000,  # 1MB máximo
                    backupCount=3,       # guarda hasta 3 archivos anteriores
                    encoding='utf-8'
                )
                file.setLevel(level)
                file.setFormatter(formatter)
                self.logger.addHandler(file)
    
    def __repr__(self) -> str:
        return f"Logger(name={self.logger.name}, level={self.logger.level})"
    
    def get_logger(self) -> log.Logger:
        return self.logger
    
    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def error(self, msg: str) -> None:
        self.logger.error(msg)

    def warning(self, msg: str) -> None:
        self.logger.warning(msg)