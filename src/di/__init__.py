from src.di.container_dao import ContainerDAO
from src.di.container_controller import ContainerController
from src.di.container_general import ContainerGeneral

di_container = ContainerGeneral()
dao_container = ContainerDAO(di_container)
controller = ContainerController(dao_container)
