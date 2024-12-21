import allure


class Endpoint:
    url = 'https://jsonplaceholder.typicode.com/posts/'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Сравниваем полученный title')
    def assert_title(self, title):
        assert self.response.json()['title'] == title

    @allure.step('Сравниваем статус запроса с 200')
    def assert_status_200(self):
        assert self.response.status_code == 200
