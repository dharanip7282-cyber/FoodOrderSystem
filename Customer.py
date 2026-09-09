class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

    def display(self):
        return f"Customer ID: {self.customer_id}\nName: {self.name}\nPhone: {self.phone}"
