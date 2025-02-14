from routes.base_routes import BaseRoutes


class CourierRoutes(BaseRoutes):
    COURIER_CREATE = "/api/v1/courier"
    COURIER_LOGIN = "/api/v1/courier/login"
    COURIER_DELETE = "/api/v1/courier/{}"

    @staticmethod
    def create_courier(data):
        return BaseRoutes.send_request("POST", CourierRoutes.COURIER_CREATE, data=data)

    @staticmethod
    def login_courier(data):
        return BaseRoutes.send_request("POST", CourierRoutes.COURIER_LOGIN, data=data)

    @staticmethod
    def delete_courier(courier_id):
        if not courier_id:
            return {"status_code": 400, "message": "Недостаточно данных для удаления курьера"}

        return BaseRoutes.send_request("DELETE", CourierRoutes.COURIER_DELETE.format(courier_id))
