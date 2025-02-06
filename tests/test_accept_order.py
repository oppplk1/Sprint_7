import allure
from routes.order_routes import OrderRoutes
from routes.courier_routes import CourierRoutes
from helpers import generate_unique_courier


@allure.epic("Orders API")
@allure.suite("Order Acceptance")
@allure.feature("Принятие заказа курьером")
class TestAcceptOrder:

    @allure.story("Курьер принимает заказ")
    @allure.title("Успешное принятие заказа курьером")
    @allure.description("Создаём курьера и заказ, затем курьер принимает заказ.")
    def test_accept_order_success(self):
        # Создаём курьера
        courier_data = generate_unique_courier()
        assert courier_data, "Не удалось создать курьера"
        login, password, _ = courier_data
        login_response = CourierRoutes.login_courier({"login": login, "password": password})
        assert login_response.status_code == 200, "Курьер не смог авторизоваться"
        courier_id = login_response.json().get("id")

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

        order_id_response = OrderRoutes.get_order_by_track(track)
        assert order_id_response.status_code == 200, "Не удалось получить orderId"

        order_data = order_id_response.json().get("order")
        assert order_data, "В ответе отсутствует объект заказа"
        order_id = order_data.get("id")

        # Принимаем заказ
        accept_response = OrderRoutes.accept_order(courier_id, order_id)
        assert accept_response.status_code == 200, "Не удалось принять заказ"
        assert accept_response.json().get("ok") is True, "Ответ не содержит {ok: true}"

        # Удаляем курьера
        CourierRoutes.delete_courier(courier_id)

    @allure.story("Попытка принятия заказа несуществующим курьером")
    @allure.title("Ошибка при принятии заказа несуществующим курьером")
    @allure.description("Курьер с ID 999999 пытается принять несуществующий заказ.")
    def test_accept_order_invalid_courier(self):
        response = OrderRoutes.accept_order(999999, 123456)
        assert response.status_code == 404, "Должна быть ошибка при принятии заказа несуществующим курьером"

    @allure.story("Попытка принятия заказа без ID курьера")
    @allure.title("Ошибка при принятии заказа без указания ID курьера")
    @allure.description("Отправляем запрос на принятие заказа, но не передаём ID курьера.")
    def test_accept_order_missing_courier_id(self):
        response = OrderRoutes.accept_order(None, 123456)
        assert response.status_code == 400, "Должна быть ошибка при отсутствии ID курьера"
