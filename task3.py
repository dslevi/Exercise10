#!/bin/env python

"""
Given list l1 and list l2, produce list l3 that contains the contents of both lists, removing duplicates
eg:
    l1 = [1,2,3]
    l2 = [2,3,4]
    
    l3 = [1,2,3,4]
"""
l1 = [1, 3, 4, 6, 8, 10]
l2 = [93, 2, 23, 77, 66]

def list_end(l1, l2):
    l3 = []
    for x in l1:
        if x not in l3:
            l3.append(x)
    for x in l2:
        if x not in l3:
            l3.append(x)
    l3.sort()
    return l3

print list_end(l1, l2)