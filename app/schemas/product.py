from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    material: Optional[str] = None
    treatment: Optional[str] = None
    spherical: Optional[int] = None
    cylindrical: Optional[int] = None
    brand: Optional[str] = None
