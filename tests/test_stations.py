# tests/test_stations.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_station():
    payload = {
        "name": "Garage Pi",
        "location": "Backyard"
    }
    response = client.post("/stations", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Garage Pi"
    assert data["location"] == "Backyard"
    assert "id" in data

def test_get_stations():
    response = client.get("/stations")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "name" in data[0]
