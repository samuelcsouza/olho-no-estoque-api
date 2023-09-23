from pymongo.database import Database
from bson import errors


class ProductRepository:
    def __init__(self, db: Database) -> None:
        self._db = db
        self._product_collection = db.get_collection('products')
        self._protected_properties = ['id']

    def _create_product_from_mongo(self, obj: dict):
        product = {k: v for k, v in obj.items() if k != "_id"}
        product["id"] = str(obj["_id"])

        return product

    def list(self):

        all = list()
        try:
            doc = self._product_collection.find({})
        except errors.InvalidId:
            raise Exception("The Id entered is not a valid ObjectId.")

        for document in list(doc):
            all.append(self._create_product_from_mongo(document))

        return all
