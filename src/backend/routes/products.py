from fastapi import APIRouter, Query
from database import products
from typing import List, Optional

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[dict])
def get_products(category: Optional[str] = Query(None)):
    if category:
        return [p for p in products if p["category"] == category]
    return products
