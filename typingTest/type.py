from time import time
import random
import tkinter as tk

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

def gui():
    # print(tk.Tcl().eval('info patchlevel'))     # check for tkinter version
    window = tk.Tk() # instance of new window
    window.geometry("800x600") # Horizontal x Vertical
    window.minsize(800, 600)
    window.maxsize(1000, 800)

    def test(): # function needs to be in the gui 
        button.destroy() # destroys the button that says "start the game"
        filename = wordBank()
        # print(filename)
        with open(filename, 'r') as file:
            original = file.read()
        label = tk.Label(window, text=original)
        label.pack()

    header = tk.Label(text = "Typing Test") # label for the window - display purposes only
    header.pack() # add the label to the window

    button = tk.Button(window, text = "Start the Game", command=test)
    button.pack(side = "bottom", padx=10, pady=5)

    window.mainloop() # display the window and label

def main():
    gui()

if __name__ == '__main__':    
    main()