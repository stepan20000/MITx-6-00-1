#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 12:46:43 2017

@author: stepan

 Problem 1 - Paying Debt off in a Year
10.0/10.0 points (graded)

Created on Wed May 31 12:46:43 2017

@author: stepan
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly 
payment required by the credit card company each month.

The following variables contain values as described below:

    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

    monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, 
print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41

instead of

Remaining balance: 813.4141998135 

So your program only prints out one thing: the remaining balance at the end of the year in the format:

Remaining balance: 4784.0

A summary of the required math is found below:

    Monthly interest rate= (Annual interest rate) / 12.0
    Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 

We provide sample test cases below. We suggest you develop your code on your own machine, and make sure your code 
passes the sample test cases, before you paste it into the box below.

Test Cases to Test Your Code With. Be sure to test these on your own machine - and that you get the same output! - 
before running your code on this webpage!
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
def PayDebtYear(bal, ann, mon): 
    b = bal - bal * mon + (ann/12) * (bal - bal * mon)
    for i in range(11):
        b = b - b * mon + (ann/12) * (b - b * mon)
    return round(b, 2)

print("Remaining balance: " + str(PayDebtYear(balance, annualInterestRate, monthlyPaymentRate)))