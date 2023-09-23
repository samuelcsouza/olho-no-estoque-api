from fastapi import Depends
from app.database import get_database
from app.repositories.product import ProductRepository
from typing import Callable
from pymongo.database import Database

from app.services.product import ProductService


def get_product_repository() -> Callable[[Database], ProductRepository]:

    def _get_repository(db=Depends(get_database)) -> ProductRepository:
        return ProductRepository(db)

    return _get_repository


def get_service(service_type: type[any]) -> Callable:

    if service_type == ProductService:
        def _service(
            product_repository: ProductRepository = Depends(
                get_product_repository()
            )
        ):
            return ProductService(
                product_repository
            )
        return _service
