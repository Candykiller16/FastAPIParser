from typing import Dict

from bson import ObjectId
from fastapi import Body

from src.models.errors import NoSneakerByThisIdError
from src.models.lamoda import Sneakers, SneakersResponse, SneakersCreateUpdate


class LamodaConnect:
    def __init__(self, db):
        self.__db = db

    """CRUD for lamoda router"""

    async def create_new_sneaker(self, sneakers: SneakersCreateUpdate = Body(...)) -> Dict[str, str]:
        new_sneaker = self.__db.db.lamoda.insert_one(sneakers)
        return {'_id': str(new_sneaker.inserted_id), **sneakers.dict()}

    async def get_sneakers(self) -> SneakersResponse:
        return SneakersResponse(clothes=list(self.__db.db.lamoda.find(limit=100)))

    async def get_sneaker_by_id(self, id: str) -> Sneakers:
        if (data := self.__db.db.lamoda.find_one({'_id': ObjectId(id)})) is not None:
            data['_id'] = str(data['_id'])
            return data
        else:
            raise NoSneakerByThisIdError

    async def update_sneaker(self, id: str, sneaker: SneakersCreateUpdate = Body(...)):
        sneakers_data = {k: v for k, v in sneaker.dict().items() if v is not None}

        if len(sneakers_data) >= 1:
            update_sneaker = self.__db.db.lamoda.update_one(
                {"_id": ObjectId(id)}, {'$set': sneakers_data}
            )
            if update_sneaker.modified_count == 0:
                raise NoSneakerByThisIdError

    async def delete_sneakers(self, id: str):
        return self.__db.db.lamoda.delete_one({'_id': ObjectId(id)})
