import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def insertor(client,vector,payload):
    request= client.post("/insert",json={
            "vector":vector,
            "payload":payload
    })
    return request
    #we r using this instead of writing insert req repeatedly

def searcher(client,vector):
    request=client.post("/search",json={
        "vector":vector
    })
    return request

def test_mt_search(client):
    response=searcher(client,[9.5,26.0,20.0])

    assert response.status_code==200
    assert response.json()["message"] == "no vectors in the database yet"

def test_insert_api(client):
    response=insertor(client,[1.0,2.0,3.0],{"name":"cat"})

    assert response.status_code==200 # in fast api 200 means no issues 404 or any other = error or smthng wrong
    assert response.json()["message"] == "vector inserted successfully"#message of succeful insert req ref main.py 

def test_search_api(client):
    insertor(client,[1.0,2.0,3.0],{"name":"cat"})
    insertor(client,[9.0,25.0,16.0],{"name":"dog"})

    response=searcher(client,[9.5,26.0,20.0])

    assert response.status_code==200
    assert response.json()["payload"]["name"]=="dog"