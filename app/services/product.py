from app.repositories.product import ProductRepository
from app.schemas.product import Product


class ProductService:
    def __init__(self, product_repository: ProductRepository) -> None:
        self._product_repository = product_repository

    def list(self):
        docs = self._product_repository.list()
        return docs

    def get(self):
        pass

    def delete(self, id: str) -> bool:
        return self._product_repository.delete(id)

    def edit(self, product: Product, id: str) -> Product:
        return self._product_repository.edit(product, id)

    def create(self, product) -> Product:
        return self._product_repository.create(product)
