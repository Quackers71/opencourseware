# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
