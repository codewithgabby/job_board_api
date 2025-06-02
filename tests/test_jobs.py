from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def get_token():
    # First, register the user (ignore if already exists)
    client.post("/users/register", json={
        "username": "pytest_user",
        "email": "pytest@example.com",
        "password": "testpass"
    })

    # Now, login to get the token
    login = client.post("/auth/login", data={
        "username": "pytest_user",
        "password": "testpass"
    })

    print("LOGIN RESPONSE:", login.json())  # debug if needed

    return login.json()["access_token"]

def test_create_job():
    token = get_token()
    response = client.post(
        "/jobs/",
        json={
            "title": "Test Job",
            "description": "A job for testing.",
            "company": "PyTest Inc.",
            "location": "Remote",
            "salary": "50000"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Job"
