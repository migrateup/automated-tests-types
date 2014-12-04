import unittest
from expensetracking import (
    Expense,
    Employee,
    reimburser,
    expensetracker,
    )

class TestPayouts(unittest.TestCase):
    def test_expenses_paid(self):
        employee = Employee('Aaron Maxwell', 128)
        expensetracker.addExpense(employee, Expense('frisbee', 7.25))
        expensetracker.addExpense(employee, Expense('hockey stick', 49.95))
        expensetracker.addExpense(employee, Expense('cool sunglasses', 29.99))

        # Total of all expenses so far is $87.19.
        self.assertEqual(87.19, expensetracker.totalUnpaidExpensesForEmployee(employee))
        # And I have not been reimbursed yet at all.
        self.assertEqual(0, expensetracker.totalPaidExpensesForEmployee(employee))
        self.assertEqual(0, reimburser.totalPaidForEmployee(employee))

        # Now the reimburser service starts the reimbursement process.
        reimburser.reimburseEmployee(employee)

        self.assertEqual(0, expensetracker.totalUnpaidExpensesForEmployee(employee))
        self.assertEqual(87.19, expensetracker.totalPaidExpensesForEmployee(employee))
        self.assertEqual(87.19, reimburser.totalPaidForEmployee(employee))

        # Let's add another expense.
        expensetracker.addExpense(employee, Expense('juice boxes', 4.50))
        self.assertEqual(4.50, expensetracker.totalUnpaidExpensesForEmployee(employee))
        self.assertEqual(87.19, expensetracker.totalPaidExpensesForEmployee(employee))
        self.assertEqual(87.19, reimburser.totalPaidForEmployee(employee))

        # ... and reimburse that one.
        reimburser.reimburseEmployee(employee)

        self.assertEqual(0, expensetracker.totalUnpaidExpensesForEmployee(employee))
        self.assertEqual(91.69, expensetracker.totalPaidExpensesForEmployee(employee))
        self.assertEqual(91.69, reimburser.totalPaidForEmployee(employee))
