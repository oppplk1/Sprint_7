import pytest
from helpers import generate_unique_courier
from routes.courier_routes import CourierRoutes


@pytest.fixture
def unique_courier():
    courier_data = generate_unique_courier()
    response = CourierRoutes.create_courier(courier_data)
    assert response.status_code == 201, "Не удалось создать курьера"
    yield courier_data
    response = CourierRoutes.login_courier({"login": courier_data["login"], "password": courier_data["password"]})
    if response.status_code == 200:
        courier_id = response.json().get("id")
        CourierRoutes.delete_courier(courier_id)
