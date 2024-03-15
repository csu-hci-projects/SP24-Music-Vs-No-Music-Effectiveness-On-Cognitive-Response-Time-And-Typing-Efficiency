from time import time
import random
import tkinter as tk

class gui(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600") # Horizontal x Vertical
        self.minsize(800, 600)
        self.maxsize(1000, 800)

        self.title("Typing Test")
        self.config(padx=50, pady=10)

        self.instructions = tk.Label(text = "Type the prompt as shown after clicking the button 'Start the Game'. The timer start at the first keystroke.") 
        self.instructions.pack() # add the label to the window

        self.file = tk.Button(self, text = "Get the Typing Test", command=self.getFile) # need to change test to function to call filename
        self.file.pack()

        # self.typingWindow = tk.Frame(self, bg='red', height=400, width=600)
        # self.typingWindow.pack(side='bottom')

        self.start = tk.Button(self, text = "Start", command=self.startUserInput)
        self.start.pack(side = "bottom", padx=10, pady=5)

        self.typingArea = tk.Text(width=100, height=20, wrap='w', padx=5, pady=5, fg='green', bg='black')
        self.typingArea.bind("<Key>", self.userInput)
        # self.typingArea.pack(side = 'bottom')

    def wordBank(self):
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

    def getFile(self):
        fileName = self.wordBank()
        # countChar = 0
        with open(fileName, 'r') as file:
            original = file.read()
            # countChar += sum(len(char) for char in original) # will be used to calculate accuracy and speed?
        # print(countChar)
        label = tk.Label(self, text=original)
        label.pack()
        self.file.destroy()

    def startUserInput(self):
        self.start.pack(side = "bottom", padx=10, pady=5)
        self.userInput()
        self.start.destroy()
    
    def userInput(self):
        print("userInput was called")
        self.typingArea.pack(side='bottom')
        self.typingArea.focus_set()






def main():
    one = gui()
    one.mainloop()

if __name__ == '__main__':    
    main()