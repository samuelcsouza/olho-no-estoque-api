from fastapi import APIRouter

from app.routes.endpoints import product

endpoint_router = APIRouter()

endpoint_router.include_router(
    product.router,
    prefix='/product',
    tags=['Produtos']
)
