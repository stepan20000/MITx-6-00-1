import math

balance = 999999
annualInterestRate = 0.18

def PayDebtYear(bal, ann, mon): 
    b = bal - mon + (ann/12) * (bal - mon)
    for i in range(11):
        b = b - mon + (ann/12) * (b - mon)
    return round(b, 2)

low = balance / 12
high = (balance * (1 + annualInterestRate / 12)**12) / 12.0 
lp = 0

lpLast = lp
b = balance

while True:
    lpLast = lp
    lp = math.ceil(100 * (low + high) / 2) / 100
    if abs(lp - lpLast) < 0.01:
        break
    b = PayDebtYear(balance, annualInterestRate, lp)
    if b > 0:
        low = lp
    elif b < -0.01:
        high = lp
    else:
        break
print("Lowest payment: " + str(lp))
