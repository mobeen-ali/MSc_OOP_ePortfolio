

"""
Demonstrates key advanced OOP concepts:
- Abstract classes (Vehicle)
- Inheritance (Car, Motorcycle)
- Polymorphism (start_engine method)
- Composition (Engine object within Vehicle)
- Aggregation (Garage class managing multiple vehicles)
"""

from abc import ABC, abstractmethod
import uuid


class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def get_specs(self):
        return f"{self.horsepower} HP, {self.fuel_type}"


class Vehicle(ABC):
    def __init__(self, brand, engine: Engine):
        self.brand = brand
        self.vehicle_id = uuid.uuid4()
        self.engine = engine

    @abstractmethod
    def start_engine(self):
        pass

    def engine_specs(self):
        return self.engine.get_specs()


class Car(Vehicle):
    def __init__(self, brand, engine: Engine, number_of_doors):
        super().__init__(brand, engine)
        self.number_of_doors = number_of_doors

    def start_engine(self):
        return f"{self.brand} car engine started with {self.engine.get_specs()}"


class Motorcycle(Vehicle):
    def __init__(self, brand, engine: Engine, has_sidecar=False):
        super().__init__(brand, engine)
        self.has_sidecar = has_sidecar

    def start_engine(self):
        return f"{self.brand} motorcycle engine roars with {self.engine.get_specs()}"


class Garage:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def list_vehicles(self):
        result = [f"{v.brand} ({v.vehicle_id}) - {v.engine_specs()}" for v in self.vehicles]
        return "\n".join(result)


# Demo
if __name__ == "__main__":
    garage = Garage("Downtown Garage")

    engine1 = Engine(150, "Petrol")
    engine2 = Engine(100, "Electric")

    car = Car("Toyota", engine1, 4)
    bike = Motorcycle("Harley-Davidson", engine2)

    garage.add_vehicle(car)
    garage.add_vehicle(bike)

    print("== Vehicle Startup ==")
    print(car.start_engine())
    print(bike.start_engine())

    print("\n== Garage Inventory ==")
    print(garage.list_vehicles())
