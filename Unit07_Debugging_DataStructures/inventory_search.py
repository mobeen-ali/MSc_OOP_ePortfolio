

"""
Demonstrates:
- Debugging and error handling
- Data structure usage (nested dictionaries, lists)
- Search algorithm (linear search)
- Best practices for clean, testable Python code
"""

import uuid


# Sample inventory using nested dictionary
inventory = {
    "P001": {"name": "Laptop", "price": 750, "stock": 10},
    "P002": {"name": "Mouse", "price": 20, "stock": 50},
    "P003": {"name": "Keyboard", "price": 35, "stock": 25},
    "P004": {"name": "Monitor", "price": 120, "stock": 15},
}


def search_product_by_name(name):
    """
    Searches for a product by its name (case-insensitive) using linear search.
    """
    for pid, details in inventory.items():
        if details["name"].lower() == name.lower():
            return pid, details
    return None


def display_product(pid, details):
    """
    Nicely formats and returns product information.
    """
    return (f"Product ID: {pid}\n"
            f"Name: {details['name']}\n"
            f"Price: ${details['price']}\n"
            f"Stock: {details['stock']} units\n")


def process_search():
    try:
        product_name = input("Enter the product name to search: ").strip()
        if not product_name:
            raise ValueError("Product name cannot be empty.")

        result = search_product_by_name(product_name)

        if result:
            pid, details = result
            print("=== Product Found ===")
            print(display_product(pid, details))
        else:
            print("Product not found in inventory.")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# pylint: disable=missing-function-docstring
# Run the system
if __name__ == "__main__":
    process_search()
