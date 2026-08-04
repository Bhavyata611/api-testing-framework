
def test_patch_post(api_client):
    payload = {
        "title": "Patched Title"
    }

    response = api_client.patch("/posts/1", payload)

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")

    data = response.json()

    assert data["title"] == payload["title"]
    assert response.elapsed.total_seconds() < 5
