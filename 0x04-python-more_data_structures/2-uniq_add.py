#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(map(lambda x: x, my_list))
    return sum(unique)
