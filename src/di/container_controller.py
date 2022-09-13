from src.controller.lamoda_controller import Lamoda


class ContainerController:
    def __init__(self, container_dao):
        self.container_dao = container_dao
        self._lamoda_controller = None

    @property
    def lamoda_controller(self):
        if self._lamoda_controller is None:
            self._lamoda_controller = Lamoda(self.container_dao)
            return self.lamoda_controller
