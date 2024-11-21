import json
from pathlib import Path

import requests
from jsonschema.validators import validate

base_url = "https://reqres.in/api/"


def resource_path(file_name):
    return Path(__file__).parent.parent.joinpath(f"schemas_files/{file_name}").absolute()


def test_validate_schema_register_user():
    payload = {
        "email": "michael.lawson@reqres.in",
        "password": "12345678"
    }
    response = requests.post(base_url + "register", json=payload)
    assert response.status_code == 200

    with open(resource_path("post_register.json")) as file:
        validate(response.json(), schema=json.loads(file.read()))


def test_validate_schema_get_users_from_third_page():
    payload = {
        "page": "3",
        "per_page": "3"
    }
    response = requests.get(base_url + "users", json=payload)
    assert response.status_code == 200

    with open(resource_path("get_user.json")) as file:
        validate(response.json(), schema=json.loads(file.read()))


def test_validate_schema_update_user_by_id():
    response = requests.put(base_url + "users/{id}")
    assert response.status_code == 200

    with open(resource_path("update_user_by_id.json")) as file:
        validate(response.json(), schema=json.loads(file.read()))


def test_validate_schema_post_user_positive():
    payload = {
        "email": "michael.lawson@reqres.in",
        "password": "12345678"
    }
    response = requests.post(base_url + "users", json=payload)
    assert response.status_code == 201

    with open(resource_path("post_user.json")) as file:
        validate(response.json(), schema=json.loads(file.read()))
