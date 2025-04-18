
"""
Demonstrates the combination of Factory and Singleton patterns.
Used to create one shared logger instance across multiple channels.

"""

from abc import ABC, abstractmethod


class Logger(ABC):
    """Abstract base logger class."""
    @abstractmethod
    def log(self, message):
        pass


class FileLogger(Logger):
    def log(self, message):
        return f"[FILE] {message}"


class ConsoleLogger(Logger):
    def log(self, message):
        return f"[CONSOLE] {message}"


class EmailLogger(Logger):
    def log(self, message):
        return f"[EMAIL] {message}"


class LoggerFactory:
    """
    Factory that ensures only one instance (Singleton) of each logger type.
    """
    _instances = {}

    @classmethod
    def get_logger(cls, logger_type):
        logger_type = logger_type.lower()
        if logger_type not in cls._instances:
            if logger_type == "file":
                cls._instances[logger_type] = FileLogger()
            elif logger_type == "console":
                cls._instances[logger_type] = ConsoleLogger()
            elif logger_type == "email":
                cls._instances[logger_type] = EmailLogger()
            else:
                raise ValueError(f"Unsupported logger type: {logger_type}")
        return cls._instances[logger_type]


# Demo
if __name__ == "__main__":
    channels = ["file", "console", "email", "email"]

    for ch in channels:
        logger = LoggerFactory.get_logger(ch)
        print(logger.log("Application event logged."))
