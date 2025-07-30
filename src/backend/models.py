from pydantic import BaseModel
from typing import List

class OrderItem(BaseModel):
    id: int
    name: str
    price: float
    category: str

class OrderRequest(BaseModel):
    customer_name: str
    product_ids: List[int]

class OrderSummary(BaseModel):
    order_id: str
    customer_name: str
    items: List[OrderItem]
    total: float
