import requests

'''Узнаем количество записей'''


def all_post():
    response = requests.get( 'https://jsonplaceholder.typicode.com/posts/').json()
    assert len(response) == 100, 'Несостыковочка'


def one_post():
    post_id = new_post()
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    # print(response)
    assert response['id'] == post_id


def post_a_post():
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
    assert response.status_code == 201
    assert response.json()['id'] == 101


def new_post():
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
    return response.json()['id']


def clear(post_id):
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


def put_a_post():
    post_id = new_post()
    body = {
        'title': 'foo---',
        'body': 'bar---',
        'userId': 2
    }
    headers = {'Content-type': 'application/json'}
    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json=body,
        headers=headers
    ).json()
    assert response['title'] == 'foo---'
    clear(post_id)


def patch_a_post():
    post_id = new_post()
    body = {
        'body': 'bar---',
    }
    headers = {'Content-type': 'application/json'}
    response = requests.patch(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json=body,
        headers=headers
    ).json()
    print(response)
    clear(post_id)


def delete_a_post():
    post_id = new_post()
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    print(response.json())
    print(response.status_code)


# all_post()
# one_post()
post_a_post()
# put_a_post()
# patch_a_post()
# delete_a_post()
