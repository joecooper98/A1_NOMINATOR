#!/usr/bin/python

import random

print("What is the name of your script?")

a = input("> ")

availableletters = ["A", "B", "C", "D", "F", "K", "M", "P", "Q", "R", "S", "T", "W", "X", "Z"]

if random.random() < 0.1:
    st = availableletters[random.randint(0,len(availableletters)-1)]+availableletters[random.randint(0,len(availableletters)-1)]
else:
    st = availableletters[random.randint(0,len(availableletters)-1)]


if random.random() < 0.15:
    no = str(random.randint(0, 999))
elif random.random() < 0.3:
    no = str(random.randint(0, 99))
else:
    no = str(random.randint(0,10))

print(st+no+"_"+a.upper())

