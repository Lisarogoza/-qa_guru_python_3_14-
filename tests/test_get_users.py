import requests
from pytest_voluptuous import S
from schemas.schemas import users_schema
import logging


def test_get_users_list():
    result = requests.get('https://reqres.in/api/users?page=2')
    logging.info(result.json())
    assert S(users_schema) == result.json()


def test_count_page():
    result = requests.get('https://reqres.in/api/users?page=2')
    per_page = result.json()['per_page']
    data = result.json()['data']

    assert per_page == 6
    assert len(data) == 6
    assert S(users_schema) == result.json()


def test_post_user():
    url = 'https://reqres.in/api/users'
    data = {'name': 'Xman', 'age': '97'}
    response = requests.post(url, data=data)

    assert response.status_code == 201
    assert response.json()['name'] == 'Xman'
    assert response.json()['age'] == '97'
