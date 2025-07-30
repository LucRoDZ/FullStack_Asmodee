from fastapi import APIRouter, Query
from typing import List, Optional
from database import products
from models import Product

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[Product])
def get_products(category: Optional[str] = Query(None)):
    if category:
        return [p for p in products if p["category"] == category]
    return products
