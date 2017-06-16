balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
def PayDebtYear(bal, ann, mon): 
    b = bal - bal * mon + (ann/12) * (bal - bal * mon)
    for i in range(11):
        b = b - b * mon + (ann/12) * (b - b * mon)
    return round(b, 2)

print("Remaining balance: " + str(PayDebtYear(balance, annualInterestRate, monthlyPaymentRate)))