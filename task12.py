#!/bin/env python

"""
Write the following two functions
    c_to_f(float) -> float
    f_to_c(float) -> float

c_to_f should convert a temperature in celsius to fahrenheit, and f_to_c should do the opposite
"""

def c_to_f(i):
    return ((i * (9.0/5)) + 32)

def f_to_c(i):
    return (i - 32) * (5.0/9)

print c_to_f(100.0)
print f_to_c(100.0)
