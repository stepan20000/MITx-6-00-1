#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 12:46:43 2017

@author: stepan

 Problem 3
15.0/15.0 points (graded)

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

"""

s = 'tnsvhcngtpmdvsoeuy'
writeA = True
a = s[0]
b = ''
aStart = 0
bStart = len(s)
for i in range(1, len(s)):
    if s[i] >= a[len(a) - 1] and writeA:
        a = a + s[i]
    elif s[i] < a[len(a) -1] and writeA:
        if len(a) > len(b) or (len(a) == len(b) and aStart < bStart):    
            writeA = False
            b = s[i]
            bStart = i
        else:
            a = s[i]
    elif s[i] >= b[len(b) - 1] and not writeA:
        b = b + s[i]
    elif s[i] < b[len(b) - 1] and not writeA:
        if len(a) > len(b) or (len(a) == len(b) and aStart < bStart):
            b = s[i]
            bStart = i
        else:
            writeA = True
            a = s[i]
            aStart = i
            
print(a, b, aStart, bStart)
if len(a) >= len(b):
    print('Longest substring in alphabetical order is: ' + a)
else:
    print('Longest substring in alphabetical order is: ' + b)