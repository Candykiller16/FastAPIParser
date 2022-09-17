import pymongo
from pymongo import MongoClient

from src.dao.mongo import Mongo
from src.di .container_general import ContainerGeneral


class ContainerDAO:
    def __init__(self, container_general: ContainerGeneral):
        self._container_general = container_general
        self._mongo = None

    @property
    def mongo_source(self) -> Mongo:
        dsn = f'mongodb://{self._container_general.config.mongodb.username}:' \
              f'{self._container_general.config.mongodb.password}@{self._container_general.config.mongodb.host}:' \
              f'{self._container_general.config.mongodb.port}'
        connection = pymongo.MongoClient(dsn)
        return Mongo(connection)
