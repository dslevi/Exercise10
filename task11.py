#!/bin/env python

"""
Write a function with the following signature:
    title(str) -> str

It should take a string and capitalize it according to book title rules
    eg:
    title("a tale of two cities")
        => A Tale of Two Cities
"""
lowercase = ["a", "of", "an", "the", "to", "at", "in", "with", "and", "for", "but", "or", "from"]

def title(my_title):
    words = my_title.split()
    title = ""
    for i in range(len(words)):
        if words[i] not in lowercase or i == 0:
            cap_word = words[i][0].upper()
            if len(words[i]) > 1:
                cap_word += words[i][1:]
            if i != 0:
                title += " "
            title += cap_word
        else:
            title += " " + words[i]
    return title

print title("cat in the hat with a bat")