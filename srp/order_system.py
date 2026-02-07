
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class OrderItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, product: Product, quantity: int):
        self.items.append(OrderItem(product, quantity))

    def total_amount(self):
        return sum(item.product.price * item.quantity for item in self.items)

class DiscountCalculator:
    def calculate_discount(self, order: Order):
        total_items = sum(item.quantity for item in order.items)
        if total_items > 3:
            return order.total_amount() * 0.1
        return 0.0

class NotificationSender:
    def send(self, message: str):
        print(f"Notification: {message}")

if __name__ == "__main__":
    ticket = Product("Concert Ticket", 50)
    vip_ticket = Product("VIP Ticket", 120)

    order = Order()
    order.add_item(ticket, 2)
    order.add_item(vip_ticket, 1)

    discount = DiscountCalculator().calculate_discount(order)
    total = order.total_amount() - discount

    NotificationSender().send(f"Your order total is ${total:.2f}")
