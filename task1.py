#!/bin/env python

"""
Given list l, sort it in reverse order
ie: 10, 9, 8, 7, 6
"""
l = [5,2,1,5,9,10,11]

def reverse(l):
    sorted_list = l.sort()
    for x in range(len(sorted_list)/2):
        temp = sorted_list[-1 - x]
        sorted_list[-1 - x] = sorted_list[x]
        sorted_list[x] = temp
    print sorted_list

reverse(l)
