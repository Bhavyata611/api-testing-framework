def test_delete_post(api_client):
    response = api_client.delete("/posts/1")

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 5


def test_delete_response_body(api_client):
    response = api_client.delete("/posts/1")

    assert response.status_code == 200

    # JSONPlaceholder returns an empty JSON object
    assert response.json() == {}