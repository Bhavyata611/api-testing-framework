import json
from jsonschema import validate


with open("schemas/post_schema.json", "r") as schema_file:
    schema = json.load(schema_file)


def test_post_schema(api_client):
    response = api_client.get("/posts/1")

    assert response.status_code == 200

    validate(instance=response.json(), schema=schema)


def test_post_contains_required_fields(api_client):
    response = api_client.get("/posts/1")

    data = response.json()

    required_fields = ["userId", "id", "title", "body"]

    for field in required_fields:
        assert field in data