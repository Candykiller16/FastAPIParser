from src.controller.lamoda_controller import LamodaController
from src.di.container_parser import ContainerParser
from src.di.container_dao import ContainerDAO
from src.di.container_general import ContainerGeneral


class ContainerController:

    def __init__(self,
                 container_general: ContainerGeneral,
                 container_dao: ContainerDAO,
                 container_lamoda: ContainerParser
                 ):
        self._container_general = container_general
        self._container_dao = container_dao
        self._container_lamoda = container_lamoda
        self._lamoda_controller = None

    @property
    def lamoda_controller(self) -> LamodaController:
        if self._lamoda_controller is None:
            self._lamoda_controller = LamodaController(
                self._container_general,
                self._container_dao,
                self._container_lamoda
            )
        return self._lamoda_controller

