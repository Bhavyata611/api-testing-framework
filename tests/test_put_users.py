
def test_update_post(api_client):
    payload = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1
    }

    response = api_client.put("/posts/1", payload)

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")

    data = response.json()

    assert data["id"] == payload["id"]
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

    assert response.elapsed.total_seconds() < 5