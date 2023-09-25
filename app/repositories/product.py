from typing import List
from pymongo.database import Database
from bson import errors, ObjectId
from app.schemas.product import Product


class ProductRepository:
    def __init__(self, db: Database) -> None:
        self._db = db
        self._product_collection = db.get_collection('products')
        self._protected_properties = ['id']

    def _create_product_from_mongo(self, obj: dict) -> Product:
        product = {k: v for k, v in obj.items() if k != "_id"}
        product["id"] = str(obj["_id"])

        return Product(**product)

    def list(self, skip: int = 0, limit: int = 10) -> List[Product]:

        all_products = list()
        documents = self._product_collection.find()\
            .skip(skip)\
            .limit(limit)

        for document in list(documents):
            all_products.append(
                self._create_product_from_mongo(document)
            )

        return all_products

    def get(self, product_id: str) -> Product:

        try:
            _product = self._product_collection.find_one(
                {"_id": ObjectId(product_id)}
            )
        except errors.InvalidId:
            raise Exception("The Id entered is not a valid ObjectId.")
        except Exception as e:
            raise Exception(f"Could not get product: {e}")

        if _product:
            _product = self._create_product_from_mongo(_product)
        else:
            raise Exception(f"Product {product_id} not found!")

        return _product

    def delete(self, product_id: str) -> bool:
        try:
            self._product_collection.delete_one(
                {"_id": ObjectId(product_id)}
            )
        except Exception as e:
            raise Exception(f"Could not delete product: {e}")

        return True

    def edit(self, product: Product, id: str) -> Product:
        new_product_dict = product.__dict__

        try:
            self._product_collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": new_product_dict}
            )
        except Exception as e:
            raise Exception(f"Could not update product: {e}")

        return self.get(id)

    def create(self, product: Product) -> Product:

        product_dict = product.__dict__

        try:
            new_product = self._product_collection.insert_one(product_dict)
        except Exception as e:
            raise Exception(f"Could not create product: {e}")

        return self.get(new_product.inserted_id)
