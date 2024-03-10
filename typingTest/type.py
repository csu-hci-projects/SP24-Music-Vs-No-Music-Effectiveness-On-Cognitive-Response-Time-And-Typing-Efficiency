from time import time
import random
import tkinter as tk

def gui():
    # check for tkinter version
    # print(tk._test())
    print(tk.Tcl().eval('info patchlevel'))


def wordBank():
    # one = "typingTest/lovestory"
    # two = "typingTest/dontstopbelievin"
    # three = "typingTest/yesterday"
    # four = "typingTest/beforehecheats"
    # five = "typingTest/hundredyears"
    one = "lovestory"
    two = "dontstopbelievin"
    three = "yesterday"
    four = "beforehecheats"
    five = "hundredyears"

    choices = [one, two, three, four, five]
    word = random.choice(choices)
    return word

def main():
    filename = wordBank()
    with open(filename, 'r') as file:
        original = file.read()
    print(original)

if __name__ == '__main__':    
    main()