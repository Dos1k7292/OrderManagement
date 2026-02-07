from abc import ABC, abstractmethod

class IPayment(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

class CreditCardPayment(IPayment):
    def process_payment(self, amount: float):
        print(f"Paid ${amount:.2f} using Credit Card.")

class PayPalPayment(IPayment):
    def process_payment(self, amount: float):
        print(f"Paid ${amount:.2f} using PayPal.")

class BankTransferPayment(IPayment):
    def process_payment(self, amount: float):
        print(f"Paid ${amount:.2f} via Bank Transfer.")

class PaymentService:
    def __init__(self, payment_method: IPayment):
        self.payment_method = payment_method

    def pay(self, amount: float):
        self.payment_method.process_payment(amount)

if __name__ == "__main__":
    payment_service = PaymentService(CreditCardPayment())
    payment_service.pay(200)
