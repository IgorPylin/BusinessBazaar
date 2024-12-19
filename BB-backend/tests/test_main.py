from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Business Bazaar API"}

def test_create_proposal():
    proposal_data = {
        "title": "Test Business",
        "description": "Test Description",
        "price": 100000.0,
        "industry": "Technology",
        "revenue": 500000.0,
        "profit": 100000.0,
        "employees_count": 10,
        "location": "Test City"
    }
    response = client.post("/proposals/", json=proposal_data)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == proposal_data["title"] 