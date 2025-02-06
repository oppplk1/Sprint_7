import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru"


class BaseRoutes:
    @staticmethod
    def send_request(method, endpoint, data=None, params=None, headers=None):
        url = f"{BASE_URL}{endpoint}"
        response = requests.request(method, url, json=data, params=params, headers=headers)
        return response
