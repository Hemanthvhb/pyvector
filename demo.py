import requests
import time

BASE_URL = "http://localhost:8000"

data = [
    ([1.0, 1.0, 1.0], {"name": "cat",        "category": "animal"}),
    ([1.0, 1.0, 2.0], {"name": "dog",        "category": "animal"}),
    ([1.0, 1.0, 3.0], {"name": "bird",       "category": "animal"}),
    ([1.0, 1.0, 4.0], {"name": "lion",       "category": "animal"}),
    ([1.0, 1.0, 5.0], {"name": "elephant",   "category": "animal"}),
    ([5.0, 5.0, 1.0], {"name": "car",        "category": "vehicle"}),
    ([5.0, 5.0, 2.0], {"name": "truck",      "category": "vehicle"}),
    ([5.0, 5.0, 3.0], {"name": "bicycle",    "category": "vehicle"}),
    ([5.0, 5.0, 4.0], {"name": "motorcycle", "category": "vehicle"}),
    ([5.0, 5.0, 5.0], {"name": "bus",        "category": "vehicle"}),
    ([9.0, 9.0, 1.0], {"name": "pizza",      "category": "food"}),
    ([9.0, 9.0, 2.0], {"name": "burger",     "category": "food"}),
    ([9.0, 9.0, 3.0], {"name": "pasta",      "category": "food"}),
    ([9.0, 9.0, 4.0], {"name": "sushi",      "category": "food"}),
    ([9.0, 9.0, 5.0], {"name": "tacos",      "category": "food"}),
]

def inserter(data):
    for vector,payload in data:
        requests.post(f"{BASE_URL}/insert", json={
                                        "vector": vector, 
                                        "payload": payload
                                     })
    print(f"{len(data)} vectors inserted successfully")

def searcher(vector,expected):
    response = requests.post(f"{BASE_URL}/search", json={
                                                    "vector": vector
                                                 })
    result=response.json()
    print(f"query : {expected}")
    print(f"result: {result['payload']['name']}({result['payload']['category']})")
    print(f"distance: {round(result['distance'],4)}")

inserter(data)

searcher([1.0, 1.0, 2.5], "a dog or bird")
searcher([5.0, 5.0, 2.5], "a truck or bicycle")
searcher([9.0, 9.0, 2.5], "a burger or pasta")