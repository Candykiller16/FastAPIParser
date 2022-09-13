from src.di.container_dao import ContainerDAO


class Lamoda:
    def __init__(self, container_dao: ContainerDAO):
        self.container_dao = container_dao

    def test(self):
        return "he"