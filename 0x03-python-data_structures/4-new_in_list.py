#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    changed_list = my_list.copy()
    if idx < 0:
        return changed_list
    elif idx > len(my_list) - 1:
        return changed_list
    else:
        changed_list[idx] = element
        return changed_list
