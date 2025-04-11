import pytest
from tests.conftest import client

@pytest.mark.asyncio
async def test_post_table():
    response = client.post("/table", json={
    "name": "test table",
    "seats": 2,
    "location": "test location"
    })

    assert response.status_code == 200
    data = response.json()
    assert data == {"status": "success"}

@pytest.mark.asyncio
async def test_get_table():
    response = client.get("/table")
    assert response.status_code == 200

def test_post_reservation():
    response = client.post("/reservation", json={
    "customer_name": "test customer",
    "table_id": 1,
    "reservation_time": "2025-04-09T14:00:00",
    "duration_minutes": 10
    })
    assert response.status_code == 200

def test_get_reservation():
    response = client.get("/reservation")
    assert response.status_code == 200


def test_delete_reservation():
    response = client.delete("/reservation/1")
    assert response.status_code == 200

def test_delete_table():
    response = client.delete("/table/1")
    assert response.status_code == 200

