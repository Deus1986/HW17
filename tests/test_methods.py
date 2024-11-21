import requests

base_url = "https://reqres.in/api/"


def test_register_user():
    payload = {
        "email": "in",
        "password": "12345678"
    }
    response = requests.post(base_url + "register", json=payload)
    assert response.status_code == 400


def test_get_users_from_third_page_three_users_on_page():
    payload = {
        "page": "3",
        "per_page": "3"
    }
    response = requests.get(base_url + "users", json=payload)
    assert response.status_code == 200


def test_update_user_by_id():
    response = requests.put(base_url + "users/{id}")
    assert response.status_code == 200


def test_delete_user_by_id():
    response = requests.delete(base_url + "users/{id}")
    assert response.status_code == 204


def test_post_user_positive():
    payload = {
        "email": "michael.lawson@reqres.in",
        "password": "12345678"
    }
    response = requests.post(base_url + "users", json=payload)
    assert response.status_code == 201

    response_json = response.json()
    assert response_json["email"] == payload.get("email")
    assert response_json["password"] == payload.get("password")


def test_get_user_by_id_negative_404():
    response = requests.put(base_url + "user")
    assert response.status_code == 404
