class FoodItem:
    def __init__(self, item_id, name, price, category):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category

    def display(self):
        return f"Item ID: {self.item_id}\nFood: {self.name}\nPrice: ₹{self.price}\nCategory: {self.category}"
