import allure
from routes.courier_routes import CourierRoutes
from helpers import generate_unique_courier
from data import ErrorMessages


@allure.epic("Courier API")
@allure.suite("Courier Creation")
@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.story("Создание курьера с уникальными данными")
    @allure.title("Успешное создание курьера")
    @allure.description("Создаём курьера, проверяем его авторизацию и удаляем после теста.")
    def test_create_courier_success(self, unique_courier, authorized_courier):
        login, password = unique_courier["login"], unique_courier["password"]

        login_response = CourierRoutes.login_courier({"login": login, "password": password})
        assert login_response.status_code == 200, "Ошибка авторизации курьера"

        courier_id = login_response.json().get("id")
        assert courier_id is not None, "ID курьера не получен после авторизации"

    @allure.story("Попытка создать курьера с дублирующимися данными")
    @allure.title("Создание курьера с одинаковыми данными должно вернуть ошибку")
    @allure.description("Создаём двух одинаковых курьеров. Ожидаем ошибку 409.")
    def test_create_duplicate_courier(self):
        courier_data = generate_unique_courier()
        login, password, first_name = courier_data
        duplicate_response = CourierRoutes.create_courier(
            {"login": login, "password": password, "firstName": first_name})
        assert duplicate_response.status_code == 409, "Можно создать двух одинаковых курьеров"
        response_json = duplicate_response.json()
        assert response_json["message"] == ErrorMessages.DUPLICATE_FIELDS_LOGIN

    @allure.story("Создание курьера без обязательных полей")
    @allure.title("Отсутствие обязательных полей при создании курьера должно вернуть ошибку")
    @allure.description("Попытка создать курьера без обязательных полей.")
    def test_create_courier_missing_fields(self):
        response = CourierRoutes.create_courier({"login": "test_user"})
        assert response.status_code == 400, "Создание курьера без обязательных полей должно возвращать ошибку"
        response_json = response.json()
        assert response_json["message"] == ErrorMessages.MISSING_FIELDS_LOGIN
