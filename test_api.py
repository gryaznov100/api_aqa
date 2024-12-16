import requests
import pytest
import allure


@pytest.fixture(scope='session')
def hello():
    print('hello')
    yield
    print('bye')


@allure.feature('Posts')
@allure.story('Get posts')
@allure.title('Создаем один пост и сравниваем его id')
@pytest.mark.smoke
def test_one_post(new_post_id,  hello):
    with allure.step(f'Отправляется GET запрос для POST с id: {new_post_id}'):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    print(response)
    with allure.step(f'Сравниваем POST id: {new_post_id}'):
        assert response['id'] == new_post_id


# '''Узнаем количество записей'''
@allure.feature('Posts')
@allure.story('Get posts')
@allure.title('Получение всех постов')
@pytest.mark.smoke
def test_get_all_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/').json()
    assert len(response) == 100, 'Несостыковочка'


@allure.feature('Posts')
@allure.story('Manipulate posts')
@allure.title('Создаем POST запрос')
@pytest.mark.tryfirst
def test_post_a_post():
    with allure.step('Подготавливаем тестовые данные'):
        body = {
            'title': 'foo',
            'body': 'bar',
            'userId': 1
        }
        headers = {'Content-type': 'application/json'}
    with allure.step('Отправляем POST запрос'):
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts/',
            json=body,
            headers=headers
        )
    with allure.step('Сравниваем статус запроса с 201'):
        assert response.status_code == 201
    with allure.step('Сравниваем полученный id с 101'):
        assert response.json()['id'] == 101


@allure.feature('Example')
@allure.story('Sum')
@allure.title('Сумма 2 + 2')
@pytest.mark.regression
def test_any():
    assert 2 + 2


@allure.feature('Example')
@allure.story('Not equals')
@allure.title('Проверка неравности 2')
@pytest.mark.parametrize('adc', [1, 22, 'sere', '345'])
def test_any_(adc):
    print(adc)
    assert adc != 2


@allure.feature('Example')
@allure.story('Not equals')
@allure.title('Сравнение 2 и 3')
def test_any_1():
    assert 2 != 3
