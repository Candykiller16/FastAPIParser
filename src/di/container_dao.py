from pymongo import MongoClient


class ContainerDAO:
    def __init__(self, container_general):
        self.container_general = container_general
        self._mongo = None

    @property
    def mongo(self):
        if self._mongo is None:
            return MongoClient(
                f"mongodb://{self.container_general.config.mongodb.username}:"
                f"{self.container_general.config.mongodb.password}@"
                f"{self.container_general.config.mongodb.host}:{self.container_general.config.mongodb.port}")
