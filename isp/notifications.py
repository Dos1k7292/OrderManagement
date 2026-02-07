from abc import ABC, abstractmethod

class IEmailNotification(ABC):
    @abstractmethod
    def send_email(self, message: str):
        pass

class ISmsNotification(ABC):
    @abstractmethod
    def send_sms(self, message: str):
        pass

class EmailNotification(IEmailNotification):
    def send_email(self, message: str):
        print(f"Email sent: {message}")

class SmsNotification(ISmsNotification):
    def send_sms(self, message: str):
        print(f"SMS sent: {message}")

if __name__ == "__main__":
    email_notifier = EmailNotification()
    email_notifier.send_email("Your order has been shipped")

    sms_notifier = SmsNotification()
    sms_notifier.send_sms("Your order is ready for pickup")
