import json

with open("test_data/payloads.json", "r") as file:
    payloads = json.load(file)


def test_patch_post(api_client):
    payload = payloads["patch_post"]

    response = api_client.patch("/posts/1", payload)

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")

    data = response.json()

    assert data["title"] == payload["title"]

    assert response.elapsed.total_seconds() < 5


def test_patch_only_updates_modified_field(api_client):
    payload = payloads["patch_post"]

    response = api_client.patch("/posts/1", payload)

    data = response.json()

    assert data["title"] == payload["title"]