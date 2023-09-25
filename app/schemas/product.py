from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    id: Optional[str] = None
    material: Optional[str] = None
    treatment: Optional[str] = None
    spherical: Optional[int] = None
    cylindrical: Optional[int] = None
    brand: Optional[str] = None


class DeletedProduct(BaseModel):
    success: bool
