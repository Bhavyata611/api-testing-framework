import pytest


def test_get_all_users(api_client):
    response = api_client.get("/users")

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")

    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 10
    assert response.elapsed.total_seconds() < 5


def test_get_single_user(api_client):
    response = api_client.get("/users/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "name" in data
    assert "username" in data
    assert "email" in data


@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_multiple_valid_users(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["id"] == user_id


def test_invalid_user(api_client):
    response = api_client.get("/users/999")

    assert response.status_code in [200, 404]

    if response.status_code == 200:
        assert response.json() == {}