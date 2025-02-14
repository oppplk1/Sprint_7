class APIEndpoints:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    COURIER_LOGIN_ENDPOINT = "/api/v1/courier/login"
    COURIER_CREATE_ENDPOINT = "/api/v1/courier"
    ORDER_CREATE_ENDPOINT = "/api/v1/orders"


class APIResponses:
    EXPECTED_SUCCESS_RESPONSE = {"ok": True}
