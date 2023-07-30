#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 16:02:48 2023

@author: emilygoff
"""

import math
print(math.pi)

#user input rad value
rad = int(input("Please enter radian value"))

#print("Your number is ",rad)

deg = rad * (180/math.pi)
print(deg)



###Create a function. Works but doesn't handle errors such as handling letters

def getrad():
    rad = int(input("Please enter radian value"))
    if rad:
        deg = rad * (180/math.pi)
        print(deg)
    else:
        print("No number provided")
    return
        
getrad()
    
#second attempt
def getrad1():
    while True:
        try:
            x = float(input("Please enter a number:").replace(',', '.').strip())
            deg = x * (180/math.pi)
            print(deg)
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            
getrad1()
