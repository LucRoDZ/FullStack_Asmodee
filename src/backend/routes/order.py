from fastapi import APIRouter, HTTPException
from database import products, orders
from models import OrderRequest, OrderSummary, OrderItem
from utils import generate_order_id
from typing import List
from data_store import save_order, load_orders

router = APIRouter(prefix="/order", tags=["Order"])

@router.post("/", response_model=OrderSummary)
def create_order(order: OrderRequest):
    if not order.customer_name.strip():
        raise HTTPException(status_code=400, detail="Le nom du client est obligatoire.")

    selected = [p for p in products if p["id"] in order.product_ids]
    if len(selected) != len(order.product_ids):
        raise HTTPException(status_code=400, detail="Un ou plusieurs IDs de produits sont invalides.")

    total = round(sum(p["price"] for p in selected), 2)
    order_id = generate_order_id()

    summary = OrderSummary(
        order_id=order_id,
        customer_name=order.customer_name,
        items=[OrderItem(**p) for p in selected],
        total=total
    )

    orders.append(summary)
    save_order(summary.model_dump())
    return summary
