from abc import ABC, abstractmethod
from srp.order_system import Order

class IDelivery(ABC):
    @abstractmethod
    def deliver_order(self, order: Order):
        pass

class CourierDelivery(IDelivery):
    def deliver_order(self, order: Order):
        print("Delivering order by courier.")

class PostDelivery(IDelivery):
    def deliver_order(self, order: Order):
        print("Delivering order by post.")

class PickUpPointDelivery(IDelivery):
    def deliver_order(self, order: Order):
        print("Order ready for pickup at point.")

if __name__ == "__main__":
    order = Order()
    delivery: IDelivery = CourierDelivery()
    delivery.deliver_order(order) 
