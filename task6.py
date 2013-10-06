#!/bin/env python

"""
Given the string s, produce a list composed of all the single characters from the original string
eg:
    s = "Hello"
    becomes
    l = {"H", "e", "l", "l", "o"}
"""
s = "Hi there, my name is Slim"

def cust_split(s):
    l = []
    for x in s:
        if x.isalpha():
            l.append(x)
    return l

print cust_split(s)