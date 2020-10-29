#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:47:09 2020

@author: robq
"""

portion_down_payment = 0.25
current_savings = 0
r = 0.04

# annual_salary = float(input("Enter your annual salary: "))
# portion_saved = float(input("Enter the % of your salary to save, as a decimal: "))
# total_cost = float(input("Enter the cost of your dream home: "))

annual_salary = 120000
portion_saved = 0.1
total_cost = 1000000

monthly_salary = annual_salary / 12
required_deposit = total_cost * portion_down_payment
monthly_savings = (annual_salary * portion_saved) / 12
saving_percentage = portion_saved * 100


print("\nYour required deposit is $",int(required_deposit))
print("Your monthly salary is $",int(monthly_salary))
print("Your Monthly Savings are $",int(monthly_savings))
print("The percentage you are saving is",int(saving_percentage),"%")

for i in range(int(current_savings), int(required_deposit)+1, int(monthly_savings)):
    while i < required_deposit+1:
        r += i
        print(i)

print(i)
print(r)
