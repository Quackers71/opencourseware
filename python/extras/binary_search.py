#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 11:05:36 2020

@author: robq
"""

# Taken from https://www.youtube.com/watch?v=zeULw-a7Mw8


data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37,40,42,45,49]
target = 37

print("data list =",data)
print("target =",target)
print("\r")


# Linear Search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            print("The target in the list was",data[i])
            return True
    print("The target no.",target,"was not found in the list!")    
    return False


# Iterative Binary Search
def binary_search_iterative(data, target):
    low = 0
    high = len(data)-1
    
    print("low is =",low)
    print("high = len(data)-1 which is =",high)
        
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            print("mid = (low + high) // 2")
            print("The element is =",data[mid])
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


# Recursive Binary Search
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            print("The data[mid] is =",data[mid])
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        else:
            return binary_search_recursive(data, target, mid+1, high)


print("linear_search outcome:",linear_search(data, target))
print("\r")
print("binary_search_iterative outcome:",binary_search_iterative(data, target))
print("\r")
print("binary_search_recursive outcome:",binary_search_recursive(data, target, 0, len(data)-1))

