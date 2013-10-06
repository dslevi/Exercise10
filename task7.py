#!/bin/env python

"""
Given the list l composed of tuples, sort the list by the second item in the tuple
    l = [(1,3), (3,2), (5,1)]
    becomes
    l = [(5,1), (3,2), (1,3)]
"""
l = [(1,2), (3,1), (17, 35), (81,20)]

def tuple_sort(l):
    new_l = []
    for x, y in l:
        new_l.append((x, y))
    new_l.sort()
    for i in range(len(l)):
        l[i] = (new_l[i][1], new_l[i][0])
    return l

print tuple_sort(l)