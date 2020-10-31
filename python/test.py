#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:35:01 2020

@author: robq
"""
import time

a = 1000
b = 1003+1
c = 1
r = 0.4
i = 0
counter = 0

print("start =",a)
print("end =",b)
print("increment =",c)
print("r is",int(r*10),"%")
print("\r")

while i < 1004:    
    for i in range(a, b, c):
        counter += 1
        print("counter is",counter)
        print("i is",i)
        print("a is",a)
        print("b is",b)
        print("c is",c)
        
        print("r is",int(r*10),"%")
        i = i + r
        print("i + r is",int(i))
        print("\r")
        
        # c += b
        # print("c + b is",c)
        # time.sleep(0.3)
        
    break

print("\ntotal of i =",int(i))
print("The Total Count is ",counter)
