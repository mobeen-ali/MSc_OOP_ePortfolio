
class Point:
    """
    A simple class to represent a point in 2D space.
    Demonstrates class definition, attributes, and basic method use.
    """

    def __init__(self, x=0, y=0):
        """Constructor method for initializing a Point."""
        self.x = x
        self.y = y

    def move(self, dx, dy):
        """Move the point by dx and dy."""
        self.x += dx
        self.y += dy

    def display(self):
        """Display the current coordinates of the point."""
        print(f"Point is at ({self.x}, {self.y})")


# Usage
if __name__ == "__main__":
    p = Point(2, 3)
    p.display()
    p.move(1, -1)
    p.display()
