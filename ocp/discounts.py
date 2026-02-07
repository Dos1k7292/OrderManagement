from abc import ABC, abstractmethod

class DiscountRule(ABC):
    @abstractmethod
    def apply_discount(self, order):
        pass

class BulkDiscount(DiscountRule):
    def apply_discount(self, order):
        total_items = sum(item.quantity for item in order.items)
        return order.total_amount() * 0.1 if total_items > 3 else 0.0

class NoDiscount(DiscountRule):
    def apply_discount(self, order):
        return 0.0

if __name__ == "__main__":
    from srp.order_system import Order, Product
    order = Order()
    order.add_item(Product("Book", 20), 5)

    discount_rule = BulkDiscount()
    discount = discount_rule.apply_discount(order)
    total = order.total_amount() - discount
    print(f"Total with discount: ${total:.2f}")
