#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = max(a_dictionary, key=lambda k: a_dictionary[k])
    return max_score
