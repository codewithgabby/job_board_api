from fastapi.testclient import TestClient
from main import app
import uuid

client = TestClient(app)

def test_register_user():
    random_suffix = str(uuid.uuid4())[:8]
    unique_username = f"pytest_user_{random_suffix}"
    unique_email = f"{unique_username}@example.com"

    response = client.post("/users/register", json={
        "username": unique_username,
        "email": unique_email,
        "password": "testpass"
    })

    assert response.status_code == 200
    assert response.json()["username"] == unique_username


def test_login_user():
    response = client.post("/auth/login", data={
        "username": "pytest_user",
        "password": "testpass"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
