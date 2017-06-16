balance = 87169
annualInterestRate = 0.18


low = balance / 12
high = (balance * (1 + annualInterestRate / 12)**12) / 12.0 

def findMinPay(balance, low, high, last):
    import math

    def PayDebtYear(bal, ann, mon): 
        b = bal - mon + (ann/12) * (bal - mon)
        for i in range(11):
            b = b - mon + (ann/12) * (b - mon)
        return round(b, 2)

    monthPay = math.ceil(100 * (low + high) / 2) / 100
    if abs(monthPay - last) < 0.01:
        return last
    b = PayDebtYear(balance, annualInterestRate, monthPay)
    if b > 0:
        return findMinPay(balance, monthPay, high, monthPay)
    elif b < 0 and  abs(monthPay - last) < 0.01  :
        return monthPay
    else:
        return findMinPay(balance, low, monthPay, monthPay)

print("Lowest payment: " + str(findMinPay(balance, low, high, 0)))
