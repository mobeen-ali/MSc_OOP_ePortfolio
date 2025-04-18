# Unit 6: Abstract Methods and Interfaces

## 🧠 Learning Focus

This unit explored the use of abstract methods and interfaces in object-oriented programming using Python. Although Python does not have formal `interface` types, abstract base classes can be used to simulate the same structure and enforce method implementation in subclasses.

Key concepts emphasized include:
- The creation and enforcement of method contracts using `abc.ABC`
- Modular and loosely coupled design
- Polymorphism through interface-style programming

## 📁 Artefact Included

### 1. Python Script – Payment Interface Simulation
- **File:** `payment_interface.py`
- **Description:** This script models a payment processing system using an abstract base class `PaymentMethod` to simulate an interface. It includes three concrete classes: `CreditCardPayment`, `PayPalPayment`, and `CryptoPayment`, each implementing the interface methods. The `PaymentProcessor` class demonstrates polymorphism by interacting with any class that implements the `PaymentMethod` interface, allowing for flexible and modular system design.

## ✅ Learning Outcomes Demonstrated

- Simulated interfaces using Python’s abstract base classes
- Enforced common behavior across multiple unrelated classes via `abstractmethod`
- Applied polymorphism to process different payment types with a single handler
- Designed modular, loosely coupled components to support future scalability
- Demonstrated best practices for interface-driven development in Python
