import json
from pathlib import Path

ORDERS_FILE = Path("orders.json")

def load_orders():
    if ORDERS_FILE.exists():
        with open(ORDERS_FILE, "r") as f:
            return json.load(f)
    return []

def save_order(order_dict):
    orders = load_orders()
    orders.append(order_dict)
    with open(ORDERS_FILE, "w") as f:
        json.dump(orders, f, indent=2)
