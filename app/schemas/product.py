from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    id: Optional[str] = None
    material: Optional[str] = None
    treatment: Optional[str] = None
    spherical: Optional[float] = None
    cylindrical: Optional[float] = None
    brand: Optional[str] = None
    value: float = 0


class DeletedProduct(BaseModel):
    success: bool
