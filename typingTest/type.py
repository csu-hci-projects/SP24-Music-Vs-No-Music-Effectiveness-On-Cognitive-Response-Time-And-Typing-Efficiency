from time import time
import random
import tkinter as tk

def gui():
    # print(tk.Tcl().eval('info patchlevel'))     # check for tkinter version
    window = tk.Tk() # instance of new window
    window.geometry("800x600") # Horizontal x Vertical
    window.minsize(800, 600)
    window.maxsize(1000, 800)

    header = tk.Label(text = "hello world") # label for the window display purposes only
    header.pack() # add the label to the window

    button = tk.Button(window, text = "Start the Game", command= window.destroy) # atm window.destroy closes the window
    button.pack(side = "bottom", padx=10, pady=5)

    window.mainloop() # display the window and label


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
    gui()
    filename = wordBank()
    with open(filename, 'r') as file:
        original = file.read()
    print(original)

if __name__ == '__main__':    
    main()