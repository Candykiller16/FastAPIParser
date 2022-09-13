from pymongo import MongoClient


class Mongo:
    def __init__(self, client: MongoClient):
        self.client = client

