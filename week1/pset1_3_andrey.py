#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 22:56:11 2017

@author: stepan
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 31 21:39:40 2017

@author: Andrey Tymofeiuk
"""

s = 'xyzabc'

longest = 0
count = 0
length = 0
order = 0

for el in range(len(s)-2):
    count = 0
    k = 0
    while s[el+k] <= s[el+k+1]:
        count += 1
        k += 1
        if el+k+1 == len(s):
            break
    if count > length:
        length = count
        order = el

longest = s[order:order + length+1]

print("Longest substring in alphabetical order is:" + longest)