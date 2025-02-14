import pytest
from helpers import generate_unique_courier
from routes.courier_routes import CourierRoutes
from routes.order_routes import OrderRoutes
from data import ORDER_DATA


@pytest.fixture
def unique_courier():
    courier_data = generate_unique_courier()
    login, password, first_name = courier_data
    courier_data = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    CourierRoutes.create_courier(courier_data)
    yield courier_data


@pytest.fixture
def authorized_courier(unique_courier):
    login, password = unique_courier["login"], unique_courier["password"]
    login_response = CourierRoutes.login_courier({"login": login, "password": password})
    courier_id = login_response.json().get("id")

    yield courier_id

    CourierRoutes.delete_courier(courier_id)


@pytest.fixture
def create_order():
    order_data = ORDER_DATA.copy()
    order_response = OrderRoutes.create_order(order_data)
    track = order_response.json().get("track")
    order_id_response = OrderRoutes.get_order_by_track(track)
    order_data = order_id_response.json().get("order")
    order_id = order_data.get("id")
    return order_id
