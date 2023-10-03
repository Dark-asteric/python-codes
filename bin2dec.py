# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 11:16:28 2023

@author: shafi.muhammad
"""

def bin2dec(str1):
    dec = 0
    n = len(str1)
    
    for i in range(0,n,1):
        pui = (n-1) - i
        dec = dec + int(str1[i])*2**pui
    return dec

str2 = '101101'
ans = bin2dec(str2)
print(ans)