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

class gui(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600") # Horizontal x Vertical
        self.minsize(800, 600)
        self.maxsize(1000, 800)

        self.header = tk.Label(text = "Typing Test") # label for the window - display purposes only
        self.header.pack() # add the label to the window

        self.start = tk.Button(self, text = "Start the Game", command=self.getFile) # need to change test to function to call filename
        self.start.pack(side = "bottom", padx=10, pady=5)

    def getFile(self):
        filename = wordBank()
        # print(filename)
        with open(filename, 'r') as file:
            original = file.read()
        label = tk.Label(self, text=original)
        label.pack()
        self.start.destroy()

def main():
    one = gui()
    one.mainloop()

if __name__ == '__main__':    
    main()