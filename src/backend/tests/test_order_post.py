from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_order_valid():
    response = client.post("/order", json={
        "customer_name": "Test User",
        "product_ids": [1, 3]
    })
    assert response.status_code == 200
    body = response.json()
    assert body["customer_name"] == "Test User"
    assert "order_id" in body
    assert len(body["items"]) == 2

def test_create_order_invalid_product_id():
    response = client.post("/order", json={
        "customer_name": "Invalid",
        "product_ids": [999]
    })
    assert response.status_code == 400

def test_create_order_empty_name():
    response = client.post("/order", json={
        "customer_name": "   ",
        "product_ids": [1]
    })
    assert response.status_code == 400
