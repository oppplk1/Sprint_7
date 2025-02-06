import allure
from routes.order_routes import OrderRoutes


@allure.epic("Order API")
@allure.suite("Get Order by Track")
@allure.feature("Получение заказа по треку")
class TestGetOrderByTrack:

    @allure.story("Получение заказа по валидному треку")
    @allure.title("Тест на получение заказа по валидному треку")
    def test_get_order_by_valid_track(self):
        # Создаём заказ
        order_data = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "Ленина 10",
            "metroStation": 4,
            "phone": "+7 999 111 22 33",
            "rentTime": 2,
            "deliveryDate": "2025-01-01",
            "comment": "Тест",
            "color": ["BLACK"]
        }
        order_response = OrderRoutes.create_order(order_data)
        assert order_response.status_code == 201, "Не удалось создать заказ"
        track = order_response.json().get("track")

        # Запрашиваем заказ по треку
        response = OrderRoutes.get_order_by_track(track)
        assert response.status_code == 200, "Не удалось получить заказ по треку"
        assert "order" in response.json(), "Ответ не содержит данных о заказе"

    @allure.story("Получение заказа по невалидному треку")
    @allure.title("Тест на получение заказа по невалидному треку")
    def test_get_order_by_invalid_track(self):
        response = OrderRoutes.get_order_by_track(999999)
        assert response.status_code == 404, "Должна быть ошибка при запросе несуществующего заказа"

    @allure.story("Получение заказа без трека")
    @allure.title("Тест на получение заказа без номера заказа")
    def test_get_order_without_track(self):
        response = OrderRoutes.get_order_by_track(None)
        assert response.status_code == 400, "Должна быть ошибка при отсутствии номера заказа"
