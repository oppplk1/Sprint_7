from routes.base_routes import BaseRoutes


class OrderRoutes(BaseRoutes):
    ORDER_CREATE = "/api/v1/orders"
    ORDER_ACCEPT = "/api/v1/orders/accept"
    ORDER_TRACK = "/api/v1/orders/track"
    ORDER_LIST = "/api/v1/orders"
    ORDER_DELETE = "/api/v1/orders/"

    @classmethod
    def create_order(cls, data):
        return cls.send_request("POST", cls.ORDER_CREATE, data=data)

    @classmethod
    def accept_order(cls, courier_id, order_id):
        params = {"courierId": courier_id}
        return cls.send_request("PUT", cls.ORDER_ACCEPT + f"/{order_id}", params=params)

    @classmethod
    def get_order_by_track(cls, track):
        params = {"t": track}
        return cls.send_request("GET", cls.ORDER_TRACK, params=params)

    @classmethod
    def get_orders_list(cls):
        return cls.send_request("GET", cls.ORDER_LIST)

    @classmethod
    def delete_order(cls, order_id):
        if not order_id:
            raise ValueError("Order ID is required")
        return cls.send_request("DELETE", cls.ORDER_DELETE.format(order_id))
