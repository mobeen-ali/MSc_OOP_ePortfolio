

"""
Demonstrates:
- Set operations (union, intersection, difference)
- Polymorphism via a common method across Car subclasses
- Recursion to count feature matches
- Linear search on a list of car objects
"""

class Car:
    def __init__(self, model, features):
        self.model = model
        self.features = set(features)

    def describe(self):
        return f"{self.model} with features: {', '.join(self.features)}"

    def has_feature(self, feature):
        return feature in self.features


class ElectricCar(Car):
    def describe(self):
        return f"Electric {super().describe()}"


class HybridCar(Car):
    def describe(self):
        return f"Hybrid {super().describe()}"


def search_by_model(cars, model_name):
    for car in cars:
        if car.model.lower() == model_name.lower():
            return car
    return None


def count_common_features(set1, set2):
    # Recursive function to count common elements
    if not set1:
        return 0
    head = next(iter(set1))
    rest = set1 - {head}
    return (1 if head in set2 else 0) + count_common_features(rest, set2)


def demonstrate_set_operations(car1, car2):
    print(f"=== Comparing {car1.model} and {car2.model} ===")
    print(f"Common Features: {car1.features & car2.features}")
    print(f"All Features: {car1.features | car2.features}")
    print(f"Unique to {car1.model}: {car1.features - car2.features}")
    print(f"Symmetric Difference: {car1.features ^ car2.features}")
    print(f"Shared Feature Count (recursive): {count_common_features(car1.features, car2.features)}")


# Demo
if __name__ == "__main__":
    car1 = ElectricCar("Tesla Model 3", ["autopilot", "touchscreen", "regenerative braking"])
    car2 = HybridCar("Toyota Prius", ["hybrid drive", "touchscreen", "eco mode"])
    car3 = Car("Honda Civic", ["manual shift", "cruise control", "eco mode"])

    cars = [car1, car2, car3]

    print("== Car Descriptions ==")
    for car in cars:
        print(car.describe())

    print("\n== Search ==")
    found = search_by_model(cars, "Tesla Model 3")
    if found:
        print("Found:", found.describe())
    else:
        print("Car not found.")

    print("\n== Set Operations ==")
    demonstrate_set_operations(car1, car2)
