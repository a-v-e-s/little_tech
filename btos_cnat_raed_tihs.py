"""
btos_cnat_raed_tihs.py
"""


import random, re, functools
import tkinter as tk


def parser(string):
    # here is our pattern:
    patt = re.compile(r'\b[A-Za-z]{4,}\b')
    # find the matches, build the new string
    new_string = ''
    for word in string.split():
        if re.fullmatch(patt, word):
            new_word = scrambler(word)
            new_string += ''.join(new_word) + ' '
        else:
            new_string += word + ' '
    # take off the last space and return it:
    new_string.rstrip(' ')
    return new_string


def scrambler(word):
    to_fill = [word[:1], word[-1:]]
    to_b_scrambled = list(word[1:-1])
    while len(to_b_scrambled):
        choice = random.choice(to_b_scrambled)
        tmp = to_fill[:-1]
        tmp.append(choice)
        tmp.append(str(to_fill[-1:][0]))
        to_fill = tmp
        to_b_scrambled.remove(choice)
    new_word = ''.join(to_fill)
    if new_word == word:
        return scrambler(word)
    else:
        return new_word