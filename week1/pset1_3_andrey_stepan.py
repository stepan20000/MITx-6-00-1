#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 22:56:11 2017

@author: stepan
"""


"""
Created on Wed May 31 21:39:40 2017

@author: Andrey Tymofeiuk
"""

s = 'jqhscjjlantjbcmgljflmy'

longest = 0
length = 0
order = 0
el = 0

while el < len(s)-2:
    k = 0
    while s[el+k] <= s[el+k+1]:
        k += 1
        if el+k+1 == len(s):
            break
    if k > length:
        length = k
        order = el
    el = el + k + 1

longest = s[order:order + length+1]

print("Longest substring in alphabetical order is:" + longest)