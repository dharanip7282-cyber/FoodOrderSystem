class Order:
    def __init__(self, order_id, customer_name, food_item, quantity):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity

    def total(self, price):
        return price * self.quantity

    def display(self, price):
        return f"Order ID: {self.order_id}\nCustomer: {self.customer_name}\nFood: {self.food_item}\nQuantity: {self.quantity}\nTotal: ₹{self.total(price)}"
