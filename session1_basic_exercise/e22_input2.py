#!/usr/bin/env python3
# Assuming a text-based command line interactive login program
# prompt to input your name
# prompt to input your password (Do not use your real password, and you may input like 12345)
# then print 'Not verified, but let you pass this time!' and exit
# -*- coding: utf-8 -*-

name = input("Input your name:")
password = input("Input your password:")

print()

print("The name your input is {}".format(name))
print("The password your input is {}".format(password))

print("Not verified, but let you pass this time!")