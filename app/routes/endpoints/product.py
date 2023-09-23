from fastapi import APIRouter, Depends, Query
from typing import Dict
from app.dependencies import get_service
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
