import requests
import random
import string
from constants import APIEndpoints


def generate_unique_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f"{APIEndpoints.BASE_URL}{APIEndpoints.COURIER_CREATE_ENDPOINT}", json=payload)

    if response.status_code == 201:
        return [login, password, first_name]
    else:
        return []
