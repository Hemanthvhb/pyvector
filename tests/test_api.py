from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_insert_api():
    response=client.post("/insert",json={
            "vector":[1.0,2.0,3.0],
            "payload": {"name":"cat"}
    })

    assert response.status_code==200
    assert response.json()["message"] == "vector inserted successfully"

def test_search_api():
    pass