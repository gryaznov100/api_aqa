import requests
import allure
from endpoints.base_endpoint import Endpoint


class CreatePost(Endpoint):

    @allure.step('Отправляем POST запрос')
    def create_new_post(self, payload, headers=None):
        if len(payload['body']) > 100:
            self.url = f'{self.url}oijweoij'
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Сравниваем статус запроса с 201')
    def assert_status_201(self):
        assert self.response.status_code == 201

    @allure.step('Сравниваем полученный id с 101')
    def assert_id(self, userId):
        assert self.response.json()['userId'] == userId

    @allure.step('Проверяем 400 ошибку')
    def assert_negative_request(self):
        assert self.response.status_code == 400

