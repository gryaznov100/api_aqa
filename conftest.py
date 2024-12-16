import requests
import pytest


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
