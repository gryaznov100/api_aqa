import requests
import pytest
from endpoints.create_post import CreatePost
from endpoints.update_post import UpdatePost


@pytest.fixture()
def new_post_id():
    body = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }
    headers = {'Content-type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts/',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    print(post_id)
    yield post_id
    print('Удаляем созданную запись')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()
