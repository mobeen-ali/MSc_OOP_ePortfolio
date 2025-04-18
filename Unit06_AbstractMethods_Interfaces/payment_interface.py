
"""
Simulates interface-based design using Python's abc module.
Demonstrates:
- Abstract base class with abstract methods
- Multiple implementing classes (CreditCard, PayPal, Crypto)
- Interface-style polymorphism
- Modularity and loose coupling via PaymentProcessor
"""

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def authorize(self, amount):
        pass

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def authorize(self, amount):
        return f"Credit Card: Authorized payment of ${amount:.2f}"

    def pay(self, amount):
        return f"Credit Card: Charged ${amount:.2f}"


class PayPalPayment(PaymentMethod):
    def authorize(self, amount):
        return f"PayPal: Payment of ${amount:.2f} authorized"

    def pay(self, amount):
        return f"PayPal: ${amount:.2f} sent successfully"


class CryptoPayment(PaymentMethod):
    def authorize(self, amount):
        return f"Crypto Wallet: Verified transfer of ${amount:.2f}"

    def pay(self, amount):
        return f"Crypto Wallet: ${amount:.2f} transferred"


class PaymentProcessor:
    def __init__(self, method: PaymentMethod):
        self.method = method

    def process_payment(self, amount):
        print(self.method.authorize(amount))
        print(self.method.pay(amount))


# Demo
if __name__ == "__main__":
    cc = CreditCardPayment()
    paypal = PayPalPayment()
    crypto = CryptoPayment()

    processor1 = PaymentProcessor(cc)
    processor2 = PaymentProcessor(paypal)
    processor3 = PaymentProcessor(crypto)

    print("=== Processing Credit Card ===")
    processor1.process_payment(50)

    print("\n=== Processing PayPal ===")
    processor2.process_payment(75)

    print("\n=== Processing Crypto ===")
    processor3.process_payment(120)
