"""
This script demonstrates key Object-Oriented Programming (OOP) concepts:
- Class and Object creation
- Constructor (__init__)
- Encapsulation (private/protected variables)
- Inheritance
- Polymorphism (method overriding)
"""

# Base class: Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # protected variable

    def introduce(self):
        return f"My name is {self.name}, and I am {self._age} years old."


# Derived class: Student inherits from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        # Polymorphism: overrides Person.introduce()
        base_intro = super().introduce()
        return f"{base_intro} I am a student with ID: {self.student_id}."


# Another derived class: Teacher
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"I am {self.name}, teaching {self.subject}."


# Demonstration
if __name__ == "__main__":
    p = Person("Alex", 35)
    s = Student("Mobeen", 29, "S12345")
    t = Teacher("Sarah", 40, "Computer Science")

    print(p.introduce())
    print(s.introduce())
    print(t.introduce())
