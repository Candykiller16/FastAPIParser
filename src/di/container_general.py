from src.config.config import Config
from fastapi import FastAPI


class ContainerGeneral:
    def __init__(self):
        self._config = Config()
        self._fastapi = FastAPI()

    @property
    def app(self) -> FastAPI:
        return self._fastapi

    @property
    def config(self) -> Config:
        return self._config
