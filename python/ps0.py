#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:06:41 2020

@author: robq
"""

import numpy

x = input("Enter a number : ")
y = input("Enter another number : ")

x = int(x)
y = int(y)

result1 = x**y
result2 = numpy.log2(x)

print("X**y =",result1)
print("log(x) =",int(result2))
