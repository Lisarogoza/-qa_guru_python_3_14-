import requests
from pytest_voluptuous import S
from requests import Response
from schemas.schemas import user_schema


def test_get_users():
    response: Response = requests.get('https://reqres.in/api/users/2')
    print(response.status_code)
    assert response.status_code == 200
    assert response.json()['data']['email'] == 'janet.weaver@reqres.in'


def test_get_user_has_avatar():
    response: Response = requests.get('https://reqres.in/api/users/2')
    print(response.status_code)
    assert response.status_code == 200
    assert response.json().get('data').get('avatar')


def test_avatar_exists():
    response: Response = requests.get('https://reqres.in/api/users/2')
    print(response.status_code)
    avatar = response.json().get('data').get('avatar')
    result = requests.get(avatar)

    assert result.status_code == 200
    assert len(response.content) != 0


def test_schema():
    response = requests.get('https://reqres.in/api/users/2')
    assert S(user_schema) == response.json()
