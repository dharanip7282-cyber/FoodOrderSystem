class Delivery:
    def __init__(self, delivery_id, order_id, address, status="Out for Delivery"):
        self.delivery_id = delivery_id
        self.order_id = order_id
        self.address = address
        self.status = status

    def display(self):
        return f"Delivery ID: {self.delivery_id}\nOrder ID: {self.order_id}\nAddress: {self.address}\nStatus: {self.status}"
