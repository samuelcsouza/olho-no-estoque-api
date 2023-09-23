from fastapi import FastAPI
from app.routes import endpoint_router


app = FastAPI()


app.include_router(endpoint_router)
