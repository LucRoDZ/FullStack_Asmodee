from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_orders():
    response = client.get("/orders")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
