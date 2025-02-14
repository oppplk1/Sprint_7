import allure
from routes.courier_routes import CourierRoutes
from helpers import generate_unique_courier
from data import ErrorMessages


@allure.epic("Courier API")
@allure.suite("Login Courier")
@allure.feature("Авторизация курьера")
class TestLoginCourier:

    @allure.story("Успешный логин курьера")
    @allure.title("Тест на успешную авторизацию курьера")
    def test_login_success(self):
        courier_data = generate_unique_courier()
        login, password, _ = courier_data
        response = CourierRoutes.login_courier({"login": login, "password": password})
        assert response.status_code == 200, "Не удалось авторизоваться"
        assert "id" in response.json(), "Ответ не содержит id курьера"
        courier_id = response.json().get("id")
        CourierRoutes.delete_courier(courier_id)

    @allure.story("Авторизация без пароля")
    @allure.title("Тест на авторизацию курьера без пароля")
    def test_login_missing_password(self):
        response = CourierRoutes.login_courier({"login": "test_user", "password": ""})
        assert response.status_code == 400, "Запрос без пароля должен возвращать 400"
        response_json = response.json()
        assert response_json["message"] == ErrorMessages.LOGIN_MISSING_DATA

    @allure.story("Авторизация без логина")
    @allure.title("Тест на авторизацию курьера без логина")
    def test_login_missing_login(self):
        response = CourierRoutes.login_courier({"login": "", "password": "test_password"})
        assert response.status_code == 400, "Запрос без пароля должен возвращать 400"
        response_json = response.json()
        assert response_json["message"] == ErrorMessages.LOGIN_MISSING_DATA

    @allure.story("Авторизация с неверными данными")
    @allure.title("Тест на авторизацию курьера с неверными данными")
    def test_login_invalid_data(self):
        response = CourierRoutes.login_courier({"login": "invalid_user", "password": "wrong_pass"})
        assert response.status_code == 404, "Запрос с несуществующими данными должен возвращать 404"
        response_json = response.json()
        assert response_json["message"] == ErrorMessages.LOGIN_INVALID_DATA
