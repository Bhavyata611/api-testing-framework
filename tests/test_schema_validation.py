import json
from jsonschema import validate





def test_post_schema(api_client):
    response = api_client.get("/posts/1")

    assert response.status_code == 200

    with open("schemas/post_schema.json", "r") as file:
        schema = json.load(file)

    validate(instance=response.json(), schema=schema)