from pydantic import BaseModel, Field
from typing import List
import uuid

class Product(BaseModel):
    id: int
    name: str
    price: float
    category: str

class OrderRequest(BaseModel):
    customer_name: str = Field(..., min_length=1)
    product_ids: List[int]

class OrderItem(Product):
    pass

class OrderSummary(BaseModel):
    order_id: str
    customer_name: str
    items: List[OrderItem]
    total: float
