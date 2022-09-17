from src.di.container_controller import ContainerController
from src.di.container_dao import ContainerDAO
from src.di.container_general import ContainerGeneral
from src.di.container_parser import ContainerParser

di_container = ContainerGeneral()
dao_container = ContainerDAO(di_container)
parser_controller = ContainerParser(di_container)
di_container_controller = ContainerController(
    di_container,
    dao_container,
    parser_controller
)
