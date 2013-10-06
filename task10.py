#!/bin/env python

s = """
Given a multiline string 's', print each line along with the line number

eg:
    mystr = "Sorry,\nMy people need me\nI must go"

    prints

    1. Sorry,
    2. My people need me
    3. I must go.

"""

mystr = "Sorry,\nMy people need me\nI must go"

def line_num(s):
    line = 1
    string = ""
    for x in range(len(s)):
        if s[x] == "\n" or x == len(s) - 1:
            if x == len(s) - 1:
                string += s[x] 
            print "%d. %s" % (line, string)
            line += 1
            string = ""
        else:
            string += s[x]

line_num(mystr)      
