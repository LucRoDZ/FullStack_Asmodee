from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_filter_products_by_category():
    response = client.get("/products?category=electronics")
    assert response.status_code == 200
    assert all(p["category"] == "electronics" for p in response.json())
