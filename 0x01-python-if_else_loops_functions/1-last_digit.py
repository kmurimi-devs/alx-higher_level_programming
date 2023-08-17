#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last = -last
string = "Last digit of {} is {} and is".format(number, last)
if last > 5:
    print(string + " greater than 5")
elif last == 0:
    print(string + " 0")
else:
    print(string + " less than 6 and not 0")
