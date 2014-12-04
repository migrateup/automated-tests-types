from collections import defaultdict
class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount
        self.is_paid = False
        
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.id = employee_id

class _ExpenseTracker:
    def __init__(self):
        # Maps employee IDs to a list of expenses
        self._expenses = dict()

    def addExpense(self, employee: Employee, expense: Expense):
        if employee.id not in self._expenses:
            self._expenses[employee.id] = list()
        self._expenses[employee.id].append(expense)
    
    def unpaidExpensesForEmployee(self, employee: Employee) -> list:
        expenses = self._expenses[employee.id]
        return [expense for expense in expenses
                    if not expense.is_paid]

    def paidExpensesForEmployee(self, employee: Employee) -> list:
        expenses = self._expenses[employee.id]
        return [expense for expense in expenses
                    if expense.is_paid]

    def totalUnpaidExpensesForEmployee(self, employee: Employee):
        return sum([expense.amount for expense in self.unpaidExpensesForEmployee(employee)])

    def totalPaidExpensesForEmployee(self, employee: Employee):
        return sum([expense.amount for expense in self.paidExpensesForEmployee(employee)])

class _Reimburser:
    def __init__(self):
        self._payout_history = defaultdict(int)

    def reimburseEmployee(self, employee: Employee):
        amount = 0
        for expense in expensetracker.unpaidExpensesForEmployee(employee):
            amount += expense.amount
            expense.is_paid = True
        self._payout_history[employee.id] += amount

    def totalPaidForEmployee(self, employee: Employee):
        return self._payout_history[employee.id]

# There can be only one.
reimburser = _Reimburser()
expensetracker = _ExpenseTracker()
