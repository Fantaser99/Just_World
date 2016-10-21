#!/usr/bin/python

import os
from sys import argv
from random import choice
from time import sleep


def gen_str():
    global curr
    for i in range(len(curr)):
        if curr[i] != text[i]:
            curr = curr[:i] + choice(list("qwertyuiopasdfghjklzxcvbnm" + text_alph)) + curr[i + 1:]


def move_cursor(x, y):
    os.system("echo -e \"\\033[" + str(y) + ";" + str(x) + "H\"")


def echo(str):
    newstr = "     " + "\n     ".join(str.split("\n"))
    print(newstr)


os.system("clear")
text = open(argv[1]).read()
text_alph = set(text)
text_alph = "".join(text_alph.difference(set(["\n", "\r", " "])))
curr = "".join([choice(list("qwertyuiopasdfghjklzxcvbnm" + text_alph * 2)) if text[i] not in [" ", "\n", "\r"] else text[i] for i in range(len(text))])
# print(curr)
while curr != text:
    move_cursor(5, 5)
    gen_str()
    echo(curr)
    # sleep(0.01)

print("\n")
