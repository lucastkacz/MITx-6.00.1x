"""
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
The following variables contain values as described below:
    >>> balance - the outstanding balance on the credit card
    >>> annualInterestRate - annual interest rate as a decimal
    >>> monthlyPaymentRate - minimum monthly payment rate as a decimal
"""

balance = 4773
annualInterestRate = 0.20
monthlyPaymentRate = 0.04

amount_periods = 12
rate = annualInterestRate / amount_periods

balance_i = balance
for _ in range(amount_periods):
    payment_i = balance_i * monthlyPaymentRate
    u_balance_i = balance_i - payment_i
    interest_i = (rate * u_balance_i)
    balance_i = u_balance_i + interest_i


print('Remaining balance: %s' % round(balance_i, 2))