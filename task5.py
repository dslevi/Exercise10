#!/bin/env python

"""
Given the string s, excise characters 6 through 12, inclusive
eg:
    s = "Hello, good sir"
    becomes 
    s = "Hello sir"
"""
s = "Hi there, my name is Slim"
n = "12345678910 1234567890"

def six_twelve(s):
    new_s = ""
    count = 0
    for x in s:
        if count < 6 or count > 12:
            new_s += x
        if x.isalpha() or x.isdigit():
            count += 1
    return new_s

print six_twelve(n)