import allure
from routes.courier_routes import CourierRoutes
from data import ErrorMessages


@allure.epic("Courier API")
@allure.suite("Courier Deletion")
@allure.feature("Удаление курьера")
class TestDeleteCourier:

    @allure.story("Удаление существующего курьера")
    @allure.title("Тест на успешное удаление курьера")
    def test_delete_courier_success(self, authorized_courier):
        courier_id = authorized_courier

        delete_response = CourierRoutes.delete_courier(courier_id)
        assert delete_response.status_code == 200, "Не удалось удалить курьера"
        assert delete_response.json().get("ok") is True, "Ответ не содержит {ok: true}"

    @allure.story("Попытка удалить несуществующего курьера")
    @allure.title("Тест на удаление курьера с неверным ID")
    def test_delete_courier_invalid_id(self):
        response = CourierRoutes.delete_courier(999999)
        assert response.status_code == 404, "Должна быть ошибка при удалении несуществующего курьера"
        response_json = response.json()
        assert response_json["message"] == ErrorMessages.DELETE_COURIER_INVALID_ID

    @allure.story("Удаление курьера без указания ID")
    @allure.title("Тест на удаление курьера без ID")
    def test_delete_courier_missing_id(self):
        response = CourierRoutes.delete_courier(None)
        assert response["status_code"] == 400, "Недостаточно данных для удаления курьера"
        assert response["message"] == ErrorMessages.DELETE_COURIER_MISSING_ID
