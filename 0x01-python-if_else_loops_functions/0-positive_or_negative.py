#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{} is positive\n".format(number))
elif number == 0:
    print(f"{} is zero\n".format(number))
else:
    print(f"{} is negative\n".format(number))
