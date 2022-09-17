from typing import Dict

from starlette.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from src.di.container_general import ContainerGeneral
from src.di.container_dao import ContainerDAO
from src.di.container_parser import ContainerParser

from src.models.lamoda import Sneakers, SneakersResponse, SneakersCreateUpdate


class LamodaController:

    def __init__(self,
                 container_general: ContainerGeneral,
                 container_dao: ContainerDAO,
                 container_parser: ContainerParser
                 ):
        self.__container_general = container_general
        self.__container_dao = container_dao
        self.__container_parser = container_parser

    """call lamoda parser"""

    async def run(self):
        await self.__container_parser.app.get_all_data()

    """calls for rest methods + http exceptions"""

    async def create_new_sneaker(self, sneaker: SneakersCreateUpdate) -> Dict[str, str]:
        return await self.__container_dao.mongo_source.lamoda_connection.create_new_sneaker(sneaker)

    async def get_sneakers(self) -> SneakersResponse:
        return await self.__container_dao.mongo_source.lamoda_connection.get_sneakers()

    async def get_sneaker_by_id(self, id: str) -> Sneakers:
        try:
            return await self.__container_dao.mongo_source.lamoda_connection.get_sneaker_by_id(id)
        except Exception as e:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Sneaker with ID {id} not found')

    async def update_sneaker(self, id: str, sneaker: SneakersCreateUpdate):
        try:
            await self.__container_dao.mongo_source.lamoda_connection.update_sneaker(id, sneaker)
        except Exception as e:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Sneaker with ID {id} not found')

    async def delete_sneaker(self, id: str):
        try:
            await self.__container_dao.mongo_source.lamoda_connection.delete_sneakers(id)
        except Exception as e:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Sneaker with ID {id} not found')
