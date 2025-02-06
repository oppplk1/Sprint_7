from routes.base_routes import BaseRoutes


class CourierRoutes(BaseRoutes):
    COURIER_CREATE = "/api/v1/courier"
    COURIER_LOGIN = "/api/v1/courier/login"
    COURIER_DELETE = "/api/v1/courier/{}"

    @classmethod
    def create_courier(cls, data):
        return cls.send_request("POST", cls.COURIER_CREATE, data=data)

    @classmethod
    def login_courier(cls, data):
        return cls.send_request("POST", cls.COURIER_LOGIN, data=data)

    @classmethod
    def delete_courier(cls, courier_id):
        if not courier_id:
            return {"status_code": 400, "message": "Courier ID is required"}

        return cls.send_request("DELETE", cls.COURIER_DELETE.format(courier_id))