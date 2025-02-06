import allure
from routes.courier_routes import CourierRoutes
from helpers import generate_unique_courier


@allure.epic("Courier API")
@allure.suite("Courier Creation")
@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.story("Создание курьера с уникальными данными")
    @allure.title("Успешное создание курьера")
    @allure.description("Создаём курьера, проверяем его авторизацию и удаляем после теста.")
    def test_create_courier_success(self):
        courier_data = generate_unique_courier()
        assert courier_data, "Не удалось создать курьера"

        login, password, first_name = courier_data
        response = CourierRoutes.login_courier({"login": login, "password": password})
        assert response.status_code == 200, "Курьер не смог авторизоваться после создания"

        courier_id = response.json().get("id")
        delete_response = CourierRoutes.delete_courier(courier_id)
        assert delete_response.status_code == 200, "Не удалось удалить курьера после теста"

    @allure.story("Попытка создать курьера с дублирующимися данными")
    @allure.title("Создание курьера с одинаковыми данными должно вернуть ошибку")
    @allure.description("Создаём двух одинаковых курьеров. Ожидаем ошибку 409.")
    def test_create_duplicate_courier(self):
        courier_data = generate_unique_courier()
        assert courier_data, "Не удалось создать первого курьера"

        login, password, first_name = courier_data
        duplicate_response = CourierRoutes.create_courier(
            {"login": login, "password": password, "firstName": first_name})
        assert duplicate_response.status_code == 409, "Можно создать двух одинаковых курьеров"

    @allure.story("Создание курьера без обязательных полей")
    @allure.title("Отсутствие обязательных полей при создании курьера должно вернуть ошибку")
    @allure.description("Попытка создать курьера без обязательных полей.")
    def test_create_courier_missing_fields(self):
        response = CourierRoutes.create_courier({"login": "test_user"})
        assert response.status_code == 400, "Создание курьера без обязательных полей должно возвращать ошибку"
