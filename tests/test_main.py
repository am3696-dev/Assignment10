from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add():
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_subtract():
    response = client.post("/subtract", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_multiply():
    response = client.post("/multiply", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 6}

def test_divide():
    response = client.post("/divide", json={"a": 6, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}

def test_divide_by_zero():
    response = client.post("/divide", json={"a": 6, "b": 0})
    assert response.status_code == 400
    # Option 1: match exact string
    assert response.json()["error"] == "Cannot divide by zero!"
