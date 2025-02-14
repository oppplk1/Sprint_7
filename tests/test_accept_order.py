import allure
from routes.order_routes import OrderRoutes
from routes.courier_routes import CourierRoutes
from data import ErrorMessages


@allure.epic("Orders API")
@allure.suite("Order Acceptance")
@allure.feature("Принятие заказа курьером")
class TestAcceptOrder:

    @allure.story("Курьер принимает заказ")
    @allure.title("Успешное принятие заказа курьером")
    @allure.description("Создаём курьера и заказ, затем курьер принимает заказ.")
    def test_accept_order_success(self, authorized_courier, create_order):
        courier_id = authorized_courier
        order_id = create_order

        accept_response = OrderRoutes.accept_order(courier_id, order_id)

        assert accept_response.status_code == 200, "Не удалось принять заказ"
        assert accept_response.json().get("ok") is True, "Ответ не содержит {ok: true}"

        CourierRoutes.delete_courier(courier_id)

    @allure.story("Попытка принятия заказа несуществующим курьером")
    @allure.title("Ошибка при принятии заказа несуществующим курьером")
    @allure.description("Курьер с ID 999999 пытается принять несуществующий заказ.")
    def test_accept_order_invalid_courier(self):
        response = OrderRoutes.accept_order(999999, 123456)
        assert response.status_code == 404, "Должна быть ошибка при принятии заказа несуществующим курьером"
        response_json = response.json()
        assert response_json["message"] == ErrorMessages.COURIER_NOT_FOUND

    @allure.story("Попытка принятия заказа без ID курьера")
    @allure.title("Ошибка при принятии заказа без указания ID курьера")
    @allure.description("Отправляем запрос на принятие заказа, но не передаём ID курьера.")
    def test_accept_order_missing_courier_id(self):
        response = OrderRoutes.accept_order(None, 123456)
        assert response.status_code == 400, "Должна быть ошибка при отсутствии ID курьера"
        response_json = response.json()
        assert response_json["message"] == ErrorMessages.MISSING_COURIER_ID
