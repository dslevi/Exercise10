#!/bin/env python

"""
Given two dictionaries, d1 and d2, merge the contents of d1 with the contents of d2, adding to the values of existing keys
eg:
    d1 = {"a": 1, "b":2}
    d2 = {"a": 3, "d": 4}

    becomes

    d1 = {"a": 4, "b":2, "d":4}

"""
d1 = {"a": 5, "c": 7, "d": 9, "q": 15}
d2 = {"a": 6, "e": 13, "g": 6, "q": 1}

def merge_dicts(d1, d2):
    for x in d2:
        if x in d1:
            d1[x] += d2[x]
        else:
            d1[x] = d2[x]
    return d1

print merge_dicts(d1, d2)