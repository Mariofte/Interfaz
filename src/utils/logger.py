import os
import logging as log
from dotenv import load_dotenv
load_dotenv()  # Carga las variables de entorno desde el archivo .env

DEBUG = os.getenv('APP_ENV', 'development') == 'development'

class Logger:
    def __init__(self, name: str):
        self.logger = log.getLogger(name)
        self.logger.setLevel(log.DEBUG if DEBUG else log.ERROR)

        if not self.logger.handlers:
            formatter = log.Formatter(
                '{%(name)s} - [%(levelname)s] | %(message)s'
            )
            console = log.StreamHandler()
            console.setFormatter(formatter)
            self.logger.addHandler(console)

    def info(self, msg: str) -> None:
        if not DEBUG: return          # silenciado en producción
        self.logger.info(msg)

    def warning(self, msg: str) -> None:
        if not DEBUG: return          # silenciado en producción
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        self.logger.error(msg)        # errores SIEMPRE se muestran