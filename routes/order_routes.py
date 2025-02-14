from routes.base_routes import BaseRoutes


class OrderRoutes(BaseRoutes):
    ORDER_CREATE = "/api/v1/orders"
    ORDER_ACCEPT = "/api/v1/orders/accept"
    ORDER_TRACK = "/api/v1/orders/track"
    ORDER_LIST = "/api/v1/orders"
    ORDER_DELETE = "/api/v1/orders/"

    @staticmethod
    def create_order(data):
        return BaseRoutes.send_request("POST", OrderRoutes.ORDER_CREATE, data=data)

    @staticmethod
    def accept_order(courier_id, order_id):
        params = {"courierId": courier_id}
        return BaseRoutes.send_request("PUT", OrderRoutes.ORDER_ACCEPT + f"/{order_id}", params=params)

    @staticmethod
    def get_order_by_track(track):
        params = {"t": track}
        return BaseRoutes.send_request("GET", OrderRoutes.ORDER_TRACK, params=params)

    @staticmethod
    def get_orders_list():
        return BaseRoutes.send_request("GET", OrderRoutes.ORDER_LIST)

    @staticmethod
    def delete_order(order_id):
        if not order_id:
            raise ValueError("Order ID is required")
        return BaseRoutes.send_request("DELETE", OrderRoutes.ORDER_DELETE.format(order_id))
