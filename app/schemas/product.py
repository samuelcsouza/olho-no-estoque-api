from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    id: Optional[str] = None
    material: Optional[str] = None
    treatment: Optional[str] = None
    spherical: Optional[float] = None
    cylindrical: Optional[float] = None
    brand: Optional[str] = None


class DeletedProduct(BaseModel):
    success: bool
