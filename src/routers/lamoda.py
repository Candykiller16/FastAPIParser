from fastapi import APIRouter, Body
from typing import List

from starlette.status import HTTP_201_CREATED

from src.di import di_container_controller
from src.models.lamoda.sneakers import Sneakers, SneakersResponse, SneakersCreateUpdate
from src.di import container_controller


router = APIRouter(
    tags=['Lamoda router'],
    prefix='/lamoda'
)


@router.get('/', response_description='Get list of all sneakers')
async def get_sneakers_list() -> SneakersResponse:
    return await di_container_controller.lamoda_controller.get_sneakers()


@router.get('/{id}', response_description='Get sneaker by id')
async def get_sneaker_by_id(id: str) -> Sneakers:
    return await di_container_controller.lamoda_controller.get_sneaker_by_id(id)


@router.put('/{id}', status_code=HTTP_201_CREATED, response_description='Update a sneaker info')
async def update_sneaker(id: str, sneaker: SneakersCreateUpdate = Body(...)):
    return await di_container_controller.lamoda_controller.update_sneaker(id, sneaker)


@router.delete('/delete', response_description='Delete a sneaker')
async def delete_sneaker(id: str):
    return await di_container_controller.lamoda_controller.delete_sneaker(id)
