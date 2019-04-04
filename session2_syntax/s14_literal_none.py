#!/usr/bin/env python3
# _*_ code:utf-8 _*_

"""literals of special literals"""

drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)