balance = 4773
annualInterestRate = 0.2

def PayDebtYear(bal, ann, mon): 
    b = bal - mon + (ann/12) * (bal - mon)
    for i in range(11):
        b = b - mon + (ann/12) * (b - mon)
    return round(b, 2)

lp = ((balance // 12) // 10 ) * 10
b = balance
while b > 0:
    lp += 10
    b = PayDebtYear(balance, annualInterestRate, lp)
    
print("Lowest payment: " + str(lp))

