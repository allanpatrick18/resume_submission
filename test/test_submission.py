from fastapi.testclient import TestClient
from app import app
client = TestClient(app)


def test_server():
    response = client.get("/")
    assert response.status_code == 200


def test_submission_ping():
    response = client.get("/submission?q=Ping")
    assert response.status_code == 200
    assert response.text == 'OK'


def test_submission_years():
    response = client.get("/submission?q=Years")
    assert response.status_code == 200
    assert response.text == '5 years'