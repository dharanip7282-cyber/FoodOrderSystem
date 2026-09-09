class Payment:
    def __init__(self, payment_id, order_id, amount, method, status="Paid"):
        self.payment_id = payment_id
        self.order_id = order_id
        self.amount = amount
        self.method = method
        self.status = status

    def display(self):
        return f"Payment ID: {self.payment_id}\nOrder ID: {self.order_id}\nAmount: ₹{self.amount}\nMethod: {self.method}\nStatus: {self.status}"
