from src.di.container_dao import ContainerDAO
from src.di.container_general import ContainerGeneral
from src.parsers.lamoda_parser import LamodaParser


class ContainerParser:
    def __init__(self, container_general: ContainerGeneral):
        self._container_general = container_general

    @property
    def app(self) -> LamodaParser:
        return LamodaParser(self._container_general)
