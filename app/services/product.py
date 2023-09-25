from typing import List
from app.repositories.product import ProductRepository
from app.schemas.product import Product
from fastapi.exceptions import HTTPException


class ProductService:
    def __init__(self, product_repository: ProductRepository) -> None:
        self._product_repository = product_repository

    def list(self, skip: int, limit: int) -> List[Product]:
        docs = self._product_repository.list(skip, limit)
        return docs

    def get(self, id: str) -> Product:
        try:
            _product = self._product_repository.get(id)
        except Exception as e:
            raise HTTPException(
                status_code=404,
                detail=str(e)
            )

        return _product

    def delete(self, id: str) -> bool:
        return self._product_repository.delete(id)

    def edit(self, product: Product, id: str) -> Product:
        return self._product_repository.edit(product, id)

    def create(self, product) -> Product:
        return self._product_repository.create(product)
