from fastapi import APIRouter, HTTPException
from database import products, orders
from models import OrderRequest, OrderSummary, OrderItem
from utils import generate_order_id
from typing import List
from data_store import save_order, load_orders

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/", response_model=List[OrderSummary])
def get_all_orders():
    return orders
