import allure
from routes.courier_routes import CourierRoutes
from helpers import generate_unique_courier


@allure.epic("Courier API")
@allure.suite("Courier Deletion")
@allure.feature("Удаление курьера")
class TestDeleteCourier:

    @allure.story("Удаление существующего курьера")
    @allure.title("Тест на успешное удаление курьера")
    def test_delete_courier_success(self):
        courier_data = generate_unique_courier()
        assert courier_data, "Не удалось создать курьера"
        login, password, _ = courier_data
        login_response = CourierRoutes.login_courier({"login": login, "password": password})
        assert login_response.status_code == 200, "Курьер не смог авторизоваться"
        courier_id = login_response.json().get("id")

        delete_response = CourierRoutes.delete_courier(courier_id)
        assert delete_response.status_code == 200, "Не удалось удалить курьера"
        assert delete_response.json().get("ok") is True, "Ответ не содержит {ok: true}"

    @allure.story("Попытка удалить несуществующего курьера")
    @allure.title("Тест на удаление курьера с неверным ID")
    def test_delete_courier_invalid_id(self):
        response = CourierRoutes.delete_courier(999999)
        assert response.status_code == 404, "Должна быть ошибка при удалении несуществующего курьера"

    @allure.story("Удаление курьера без указания ID")
    @allure.title("Тест на удаление курьера без ID")
    def test_delete_courier_missing_id(self):
        response = CourierRoutes.delete_courier(None)
        assert response["status_code"] == 400, "Ошибка удаления остуствующего id курьера"
        assert "Courier ID is required" in response["message"], "Ошибка должна содержать информацию о необходимости ID"
