# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 18:08:11 2023

@author: Shafi
"""

import re

password = input("Enter your password : ")

if len(password)<8:
    print("Password must be at least 8 character.")
elif not re.search('[A-Z]', password):
    print("Password must be contained at one capital letter.")
elif not re.search('[a-z]',password):
    print("Password must be contained at least one smaller letter.")
elif not re.search("[0-9]",password):
    print("Password must be contained at least one number.")
elif not re.search("[&,%,$,@,#,{,},(,),/,!,*,-,_,;,:,§,=]",password):
    print("Password must be contained at least one special charecter.")
else:
    print("Your password is strong enough. So, don't worry.")