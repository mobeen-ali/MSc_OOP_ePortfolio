
"""
Implements the Factory Design Pattern for a Notification System.
Demonstrates memory safety in Python and sustainable object creation.

"""

from abc import ABC, abstractmethod


class Notification(ABC):
    """
    Abstract base class for notifications.
    """
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        return f"[EMAIL] {message}"


class SMSNotification(Notification):
    def send(self, message):
        return f"[SMS] {message}"


class PushNotification(Notification):
    def send(self, message):
        return f"[PUSH] {message}"


class NotificationFactory:
    """
    Factory class to generate Notification objects based on type.
    """
    @staticmethod
    def create_notification(channel):
        channel = channel.lower()
        if channel == "email":
            return EmailNotification()
        elif channel == "sms":
            return SMSNotification()
        elif channel == "push":
            return PushNotification()
        else:
            raise ValueError(f"Unsupported channel: {channel}")


# Demo (simulating user selection)
if __name__ == "__main__":
    channels = ["email", "sms", "push", "fax"]

    for ch in channels:
        try:
            notifier = NotificationFactory.create_notification(ch)
            print(notifier.send("System alert triggered."))
        except ValueError as ve:
            print(f"Error: {ve}")
