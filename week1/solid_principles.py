from abc import ABC, abstractmethod


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order_id: str, items: list, total: float) -> None:
        pass


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass


# Separate Notification systems -> Interface Segregation (ISP)
class EmailNotification(ABC):
    @abstractmethod
    def send_email(self, message: str) -> None:
        pass


class SMSNotification(ABC):
    @abstractmethod
    def send_sms(self, message: str) -> None:
        pass


# Implementation of concrete methods (SRP, OCP, LSP)


class MySQLOrderRepository(OrderRepository):
    def save(self, order_id: str, items: list, total: float):
        print(f"Saved order {order_id} totalling ${total} to MySQL.")


class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Successfully processed ${amount} via Stripe.")
        return True


class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Successfully processed ${amount} via PayPal.")
        return True


class NotificationService(EmailNotification):
    def send_email(self, message: str):
        print(f"Notification Email sent: {message}")


# Validator performs only validation -> SRP
class OrderValidator:
    @staticmethod
    def validate(items: list) -> bool:
        if not items:
            print("Validation Failed: Order is empty.")
            return False
        return True


class OrderProcessor:
    def __init__(
        self,
        repository: OrderRepository,
        payment_processor: PaymentProcessor,
        notifier: EmailNotification,
    ):
        self.repository = repository
        self.payment_processor = payment_processor
        self.notifier = notifier

    def process(self, order_id: str, items: list, total_amount: float):
        if not OrderValidator.validate(items):
            return
        payment_success = self.payment_processor.process_payment(total_amount)

        if payment_success:
            self.repository.save(order_id, items, total_amount)
            self.notifier.send_email(f"Your order {order_id} was successful!")


db = MySQLOrderRepository()
stripe_payment = StripePaymentProcessor()
email_service = NotificationService()


processor = OrderProcessor(
    repository=db, payment_processor=stripe_payment, notifier=email_service
)

print("Processing Order 1")
processor.process("ORD-1001", ["Laptop", "Mouse"], 1250.00)


print("\n--- Business Pivots: Switching to PayPal ---")

paypal_payment = PayPalPaymentProcessor()

paypal_processor = OrderProcessor(
    repository=db, payment_processor=paypal_payment, notifier=email_service
)
paypal_processor.process("ORD-1002", ["Keyboard"], 75.00)

"""
O/P:
Processing Order 1
Successfully processed $1250.0 via Stripe.
Saved order ORD-1001 totalling $1250.0 to MySQL.
Notification Email sent: Your order ORD-1001 was successful!

--- Business Pivots: Switching to PayPal ---
Successfully processed $75.0 via PayPal.
Saved order ORD-1002 totalling $75.0 to MySQL.
Notification Email sent: Your order ORD-1002 was successful!
"""