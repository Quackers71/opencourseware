#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 12:46:10 2020

@author: robq
"""

# x = float(input("Enter a num for x: "))
# y = float(input("Enter a num for y: "))
# if x == y:
#     print("x and y are equal!")
#     if y != 0:
#         print("Therefore, x / y is", x/y)
# elif x < y:
#     print("\nx is a smaller number")
# else:
#     print("\ny is a smaller number")
    
# print("\nThanks Yo!")


# n = input("You are still in the the Lost Forest\nGo left (l) or right (r) ? ")
# while n == "r" or n == "R":
#     n = input("You are still in the Lost Forest\nGo left (l) or right (r) ? ")

# print("\nYou made it out of the Lost Forest!\n\n              \o/")

## more complicated with while loop
# n = 0
# while n < 5:
#     print(n+1)
#     n = n + 1

## shortcut with for loop
# for n in range(5):
#     print(n+1)

## range(start,stop,step)
# mysum = 0
# for i in range(7, 10):
#     mysum += i
#     print(i,mysum)
# print(mysum)

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    print(i,mysum)
print(mysum)
