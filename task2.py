#!/bin/env python

"""
Given dictionary d, print out the key-value pairs in alphabetical order by key, separated by commas
eg:
a, 1
b, 2
c, 4
d, 6
"""
d = {"q": 5, "m": 3, "z":2, "a": 10}

def alpha_keys(d):
    key_list = d.keys()
    key_list.sort()
    for key in key_list:
        print key + ", " + str(d[key])   

alpha_keys(d)
