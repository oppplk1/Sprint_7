import allure
from routes.order_routes import OrderRoutes


@allure.epic("Orders API")
@allure.suite("Order List")
@allure.feature("Получение списка заказов")
@allure.story("API /orders возвращает список заказов")
@allure.title("Проверка, что API возвращает код 200 и список заказов")
@allure.description("Этот тест проверяет, что API корректно возвращает список заказов")
class TestGetOrdersList:
    def test_get_orders_list(self):
        response = OrderRoutes.get_orders_list()
        assert response.status_code == 200, "Не удалось получить список заказов"
        assert "orders" in response.json(), "Ответ не содержит список заказов"
