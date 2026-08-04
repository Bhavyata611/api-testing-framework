import json

with open("test_data/payloads.json", "r") as file:
    payloads = json.load(file)


def test_update_post(api_client):
    payload = payloads["updated_post"]

    response = api_client.put("/posts/1", payload)

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")

    data = response.json()

    assert data["id"] == payload["id"]
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

    assert response.elapsed.total_seconds() < 5


def test_put_response_contains_required_fields(api_client):
    payload = payloads["updated_post"]

    response = api_client.put("/posts/1", payload)

    data = response.json()

    required_fields = ["id", "title", "body", "userId"]

    for field in required_fields:
        assert field in data