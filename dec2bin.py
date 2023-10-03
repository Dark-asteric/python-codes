# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 11:05:05 2023

@author: shafi.muhammad
"""

def dec2bin(n):
    res = ""
    while n>=1:
        r = n%2
        res = str(r) + res
        n = n//2
    return res
#n= int(45)
ans = dec2bin(13)
print(ans)