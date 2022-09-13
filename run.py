import uvicorn
from src.di import di_container
from src.app import main
from src.routers.lamoda import lamoda_routers

di_container.app.include_router(
    router=lamoda_routers,
    prefix="/lamoda"
)
if __name__ == "__main__":
    uvicorn.run(di_container.app, host=di_container.config.service.host, port=di_container.config.service.port,
                log_level=di_container.config.service.log_level)
