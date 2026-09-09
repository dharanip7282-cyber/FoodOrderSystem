from Customer import Customer
from FoodItem import FoodItem
from Order import Order
from Payment import Payment
from Delivery import Delivery

def main():
    print("=" * 45)
    print("          FOOD ORDER SYSTEM")
    print("=" * 45)

    customer = Customer(101, "Rahul", "9876543210")
    food = FoodItem(201, "Veg Burger", 150, "Fast Food")
    order = Order(301, customer.name, food.name, 2)
    total = order.total(food.price)
    payment = Payment(401, order.order_id, total, "UPI")
    delivery = Delivery(501, order.order_id, "Chennai, Tamil Nadu")

    print("\n--- Customer ---")
    print(customer.display())
    print("\n--- Food Item ---")
    print(food.display())
    print("\n--- Order ---")
    print(order.display(food.price))
    print("\n--- Payment ---")
    print(payment.display())
    print("\n--- Delivery ---")
    print(delivery.display())
    print("\nFood order processed successfully.")

if __name__ == "__main__":
    main()
