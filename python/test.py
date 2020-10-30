#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:35:01 2020

@author: robq
"""

portion_down_payment = 0.25
current_savings = 0
r = 0.04

a = 0
b = 250001
c = 1000
r = 0.4
i = 0

while i < b:
    for i in range(a, b, c):
        i += r*100
        print(int(i))
               
    break



# while current_savings < 25:
#     for i in range()
#     current_savings+=1
