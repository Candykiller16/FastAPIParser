from pymongo import MongoClient

from src.config.config import Config
from src.dao.connect.lamoda_connect import LamodaConnect


class Mongo:
    def __init__(self, db):
        self.__db = db
        self.__lamoda = LamodaConnect(self.__db)

    @property
    def lamoda_connection(self) -> LamodaConnect:
        return self.__lamoda


