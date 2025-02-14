import allure
from routes.order_routes import OrderRoutes
from data import ORDER_DATA
from data import ErrorMessages


@allure.epic("Order API")
@allure.suite("Get Order by Track")
@allure.feature("Получение заказа по треку")
class TestGetOrderByTrack:

    @allure.story("Получение заказа по валидному треку")
    @allure.title("Тест на получение заказа по валидному треку")
    def test_get_order_by_valid_track(self):
        order_data = ORDER_DATA.copy()
        order_response = OrderRoutes.create_order(order_data)
        track = order_response.json().get("track")
        response = OrderRoutes.get_order_by_track(track)
        assert response.status_code == 200, "Не удалось получить заказ по треку"
        assert "order" in response.json(), "Ответ не содержит данных о заказе"

    @allure.story("Получение заказа по невалидному треку")
    @allure.title("Тест на получение заказа по невалидному треку")
    def test_get_order_by_invalid_track(self):
        response = OrderRoutes.get_order_by_track(999999)
        assert response.status_code == 404, "Должна быть ошибка при запросе несуществующего заказа"
        response_json = response.json()
        assert response_json["message"] == ErrorMessages.GET_ORDER_WITH_INVALID_TRACK

    @allure.story("Получение заказа без трека")
    @allure.title("Тест на получение заказа без номера заказа")
    def test_get_order_without_track(self):
        response = OrderRoutes.get_order_by_track(None)
        assert response.status_code == 400, "Должна быть ошибка при отсутствии номера заказа"
        response_json = response.json()
        assert response_json["message"] == ErrorMessages.GET_ORDER_WITHOUT_TRACK
