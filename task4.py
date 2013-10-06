#!/bin/env python

"""
Given the string s, split it into two strings, s2 and s3, s2 containing the first 5 letters of the string, and s3 containing the remaining letters.

eg:
    s1 = "Hello there"
    s2 = "Hello"
    s3 = " there"

"""
s = "Hi there, my name is Slim"

def first_five(str):
    s2 = ""
    s3 = ""
    count = 0
    for x in str:
        if count < 5:
            s2 += x
        else:
            s3 += x
        if x.isalpha():
            count += 1
    print "s2 = '%s', s3 = '%s'" % (s2, s3)

first_five(s)
