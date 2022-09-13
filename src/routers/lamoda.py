from fastapi import APIRouter
from src.di import container_controller
lamoda_routers = APIRouter()

@lamoda_routers.get("/hello/{name}")
async def say_hello(name: str):
    container_controller.Lamoda.test()
    return {"message": f"Hello {name}"}