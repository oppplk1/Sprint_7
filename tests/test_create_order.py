import pytest
import allure
from routes.order_routes import OrderRoutes
from data import ORDER_DATA


@allure.epic("Order API")
@allure.suite("Order Creation")
@allure.feature("Создание заказа")
class TestCreateOrder:
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    @allure.story("Создание заказа с различными цветами")
    @allure.title("Тест на создание заказа с параметрами цвета")
    def test_create_order_success(self, color):
        order_data = ORDER_DATA.copy()
        order_data["color"] = color

        response = OrderRoutes.create_order(order_data)
        assert response.status_code == 201, "Не удалось создать заказ"
        assert "track" in response.json(), "Ответ не содержит track заказа"
