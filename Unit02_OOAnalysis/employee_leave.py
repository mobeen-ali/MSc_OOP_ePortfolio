# Extension Activity

class Employee:
    """
    Base class for an employee.
    """
    def __init__(self, name, leave_balance):
        self.name = name
        self._leave_balance = leave_balance  # Protected variable

    def view_balance(self):
        return f"{self.name} has {self._leave_balance} days of leave left."


class HRAdmin(Employee):
    """
    Inherits from Employee. Can approve leave.
    """
    def approve_leave(self, days_requested):
        if days_requested <= self._leave_balance:
            self._leave_balance -= days_requested
            return f"Leave approved. Remaining: {self._leave_balance} days."
        else:
            return "Leave request exceeds balance."


# Sample usage
if __name__ == "__main__":
    emp = HRAdmin("Mobeen", 10)
    print(emp.view_balance())
    print(emp.approve_leave(5))
    print(emp.view_balance())
