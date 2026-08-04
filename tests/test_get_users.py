
def test_get_users(api_client):
    response = api_client.get("/users")

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    assert response.elapsed.total_seconds() < 2
