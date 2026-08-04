
def test_create_post(api_client):
    payload = {
        "title": "QA Framework",
        "body": "Testing POST API",
        "userId": 1
    }

    response = api_client.post("/posts", payload)

    assert response.status_code == 201
    assert response.headers["Content-Type"].startswith("application/json")

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data

    assert response.elapsed.total_seconds() < 5