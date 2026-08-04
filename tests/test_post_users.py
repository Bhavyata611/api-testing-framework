import json


with open("test_data/payloads.json", "r") as file:
    payloads = json.load(file)


def test_create_post(api_client):
    payload = payloads["valid_post"]

    response = api_client.post("/posts", payload)

    assert response.status_code == 201
    assert response.headers["Content-Type"].startswith("application/json")

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data

    assert response.elapsed.total_seconds() < 5


def test_create_post_with_empty_payload(api_client):
    payload = payloads["empty_payload"]

    response = api_client.post("/posts", payload)

    assert response.status_code == 201

    assert "id" in response.json()


def test_response_contains_required_fields(api_client):
    payload = payloads["valid_post"]

    response = api_client.post("/posts", payload)

    data = response.json()

    required_fields = ["id", "title", "body", "userId"]

    for field in required_fields:
        assert field in data