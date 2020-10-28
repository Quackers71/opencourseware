#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:24:19 2020

@author: robq
"""

i = 3
j = 2

print("i + j =",i+j)
print("i - j =",i-j)
print("i * j =",i*j)
print("i / j =",i/j)

print("The remainder when i is divided by j = ",i%j)
print("i to the power of j = ",i**j)

pi = 3.14159
radius = 2.2
area = pi*(radius**2)

print("\nThe area is ",round(area,2))

radius += 1
area = pi*(radius**2)

print("\nThe New area is ",round(area,2))
