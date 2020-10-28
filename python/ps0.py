#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:06:41 2020

@author: robq
"""

import numpy

x = int(input("Enter a number : "))
y = int(input("Enter another number : "))

result1 = x**y
result2 = numpy.log2(x)

print("X**y =",result1)
print("log(x) =",int(result2))
