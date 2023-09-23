from app.repositories.product import ProductRepository


class ProductService:
    def __init__(self, product_repository: ProductRepository) -> None:
        self._product_repository = product_repository

    def list(self):
        docs = self._product_repository.list()
        return docs
