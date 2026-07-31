from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_home():

    response = client.get("/")

    assert response.status_code == 201

    assert response.json() == {
        "message": "Welcome to Smart Expense Tracker API"
    }

def test_add_expense():

    response = client.post(
        "/expenses",
        json={
            "title": "Coffee",
            "amount": 150,
            "category": "Food",
            "date": "2026-07-31"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Coffee"
    assert data["amount"] == 150
    assert data["category"] == "Food"
    assert data["date"] == "2026-07-31"
    assert "id" in data

def test_get_expenses():

    response = client.get("/expenses")

    assert response.status_code == 201

    data = response.json()

    assert isinstance(data, list)

def test_filter_by_category():

    response = client.get("/expenses?category=Food")

    assert response.status_code == 201

    data = response.json()

    assert isinstance(data, list)

    for expense in data:
        assert expense["category"].lower() == "food"

def test_total_expenses():

    response = client.get("/expenses/total")

    assert response.status_code == 201

    data = response.json()

    assert "total" in data

def test_delete_expense():

    response = client.post(
        "/expenses",
        json={
            "title":"Temporary",
            "amount":100,
            "category":"Misc",
            "date":"2026-07-31"
        }
    )

    expense = response.json()

    delete = client.delete(
        f"/expenses/{expense['id']}"
    )

    assert delete.status_code == 200

    assert delete.json()["message"] == "Expense deleted successfully"

    
def test_invalid_amount():

    response = client.post(
        "/expenses",
        json={
            "title":"Pizza",
            "amount":-100,
            "category":"Food",
            "date":"2026-07-31"
        }
    )

    assert response.status_code == 422