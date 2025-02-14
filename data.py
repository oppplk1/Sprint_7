ORDER_DATA = {
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


class ErrorMessages:
    COURIER_NOT_FOUND = "Курьера с таким id не существует"
    MISSING_COURIER_ID = "Недостаточно данных для поиска"
    DUPLICATE_FIELDS_LOGIN = "Этот логин уже используется. Попробуйте другой."
    MISSING_FIELDS_LOGIN = "Недостаточно данных для создания учетной записи"
    DELETE_COURIER_INVALID_ID = "Курьера с таким id нет."
    DELETE_COURIER_MISSING_ID = "Недостаточно данных для удаления курьера"
    GET_ORDER_WITHOUT_TRACK = "Недостаточно данных для поиска"
    GET_ORDER_WITH_INVALID_TRACK = "Заказ не найден"
    LOGIN_MISSING_DATA = "Недостаточно данных для входа"
    LOGIN_INVALID_DATA = "Учетная запись не найдена"