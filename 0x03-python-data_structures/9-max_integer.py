#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if len(my_list) == 0:
        return None
    else:
        for num in my_list:
            if num > max:
                max = num
        return max
