"""
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. 
By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
"""

balance = 4773
annualInterestRate = 0.20

amount_periods = 12
rate = annualInterestRate / amount_periods

def calculate_balance_fixed(balance, rate, fixedPaymet):
    balance_i = balance
    payment_i = fixedPaymet
    for _ in range(amount_periods):
        u_balance_i = balance_i - payment_i
        interest_i = (rate * u_balance_i)
        balance_i = u_balance_i + interest_i
    return balance_i

lowest_payment = 10
while calculate_balance_fixed(balance, rate, lowest_payment) > 0:
    lowest_payment += 10


print('Lowest Payment: %s' % lowest_payment)