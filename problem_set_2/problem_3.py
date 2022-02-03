"""
We can make this program run faster using a technique introduced in lecture - bisection search!
"""

balance = 999999
annualInterestRate = 0.18

amount_periods = 12
rate = annualInterestRate / amount_periods

epsilon = 0.01

def calculate_balance_fixed(balance, rate, fixedPaymet):
    balance_i = balance
    payment_i = fixedPaymet
    for _ in range(amount_periods):
        u_balance_i = balance_i - payment_i
        interest_i = (rate * u_balance_i)
        balance_i = u_balance_i + interest_i
    return balance_i


lower_bound = balance / amount_periods          # Case where there isn't any interests
upper_bound = (balance * (1 + rate)**12) / 12   # lower_bound plus the interest rate in a year


while abs(calculate_balance_fixed(balance, rate, lower_bound)) > epsilon:
    mid_point = (lower_bound + upper_bound) / 2
    if calculate_balance_fixed(balance, rate, mid_point) > 0:
        lower_bound = mid_point
    else:
        upper_bound = mid_point


print('Lowest Payment: %s' % round(lower_bound, 2))