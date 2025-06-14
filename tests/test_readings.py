from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_reading():
    # First create the station this reading will belong to
    station_payload = {
        "name": "Test Station",
        "location": "Test Location"
    }
    station_resp = client.post("/stations", json=station_payload)
    assert station_resp.status_code == 200
    station_id = station_resp.json()["id"]

    # Now create the reading using that station ID
    reading_payload = {
        "station_id": station_id,
        "temperature": 22.5,
        "humidity": 55.0
    }

    response = client.post("/readings", json=reading_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["station_id"] == station_id
    assert "id" in data
    assert "timestamp" in data

def test_get_readings():
    response = client.get("/readings")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:  # if any readings exist
        assert "temperature" in data[0]
        assert "timestamp" in data[0]
