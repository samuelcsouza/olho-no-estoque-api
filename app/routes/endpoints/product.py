from fastapi import APIRouter, Depends, Query
from typing import Dict
from app.dependencies import get_service
from app.schemas.product import Product
from app.services.product import ProductService


router = APIRouter()


@router.get("")
def list(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=0, le=100),
    service: ProductService = Depends(get_service(ProductService)),
) -> Dict:

    list = service.list()

    return {
        "skip": skip,
        "limit": limit,
        "data": list
    }


@router.post("/new", status_code=201)
def create_product(
    product: Product,
    service: ProductService = Depends(get_service(ProductService)),
) -> Product:

    new = service.create(product)

    return new


@router.patch("/edit/{id}")
def update_product(
    id: str,
    product: Product,
    service: ProductService = Depends(get_service(ProductService)),
) -> Product:

    updated_product = service.edit(product, id)

    return updated_product
