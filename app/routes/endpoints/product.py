from fastapi import APIRouter, Query
from typing import Dict


router = APIRouter()


@router.get("")
def list(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=0, le=100),
) -> Dict:

    return {
      "skip": skip,
      "limit": limit,
      "data": []
    }
