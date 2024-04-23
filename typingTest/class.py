# from time import time
import time
import random
import tkinter as tk
from tkinter.font import Font
from csv import *

class gui(tk.Tk):
    def __init__(self):
        super().__init__()

        maxHeight = self.winfo_screenheight()
        maxWidth = self.winfo_screenwidth()
        self.geometry(f"{maxWidth}x{maxHeight}") # Horizontal x Vertical
        self.minsize(800, 700)

        self.title("Typing Test")
        self.text_font = Font(family='Arial', size=20)

        self.instructions = tk.Label(wraplength=700, justify='center',font=self.text_font, text = "Type the prompt. The timer starts at the first keystroke. To end the typing portion, use the mouse to hit done.") 

        self.instructions.pack() # add the label to the window

        self.file = tk.Button(self, text = "Get the Typing Test", command=self.getFile)
        self.file.pack()

        self.typingWindow = tk.Frame(width=200, height=40, padx=5, pady=5)
        self.typingWindow.place(x=375, y=300)

        self.typingArea = tk.Text(self.typingWindow, wrap='w', padx=5, pady=5, fg='black', bg='white', font=self.text_font)
        self.typingArea.pack()

        self.done = tk.Button(self, text='Done', command=self.checkResults)

        self.song = ""
        self.inputWords = []
        self.inputFromUser = []
        self.totalWords = len(self.inputWords)
        self.startTime = 0
        self.endTime = 0
        self.accuracy = 0
        self.csv_file = []

        self.mainloop()

    def wordBank(self):
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
        with open(fileName, 'r') as file:
            original = file.read()
            self.song = original
            self.inputWords = original.split()
            self.totalWords = len(self.inputWords)
        label = tk.Label(self, text=original, font=self.text_font)
        label.pack()
        self.file.destroy()
        self.userInput()

    def userInput(self):
        self.typingArea.pack(side='bottom')
        self.typingArea.focus_set()
        self.startTime = time.time()
        self.done.pack()

    def userAccuracy(self):
        temp = self.typingArea.get("1.0", 'end-1c')
        self.inputFromUser = temp.split()
        self.accuracy = (sum(1 for x,y in zip(self.inputWords, self.inputFromUser) if x ==y) / self.totalWords) * 100
        if self.accuracy < 100:
            accuracyLabel = tk.Label(self, text = f'{self.accuracy:.3}% accuracy', font=self.text_font)
            self.csv_file.append(accuracyLabel.cget("text"))
        else:
            accuracyLabel = tk.Label(self, text = f'{self.accuracy}% accuracy', font=self.text_font)
            self.csv_file.append(accuracyLabel.cget("text"))
        accuracyLabel.pack()
        self.typingArea.destroy()
        saveButton = tk.Label(self,text="Results Saved", font=self.text_font,  command=self.save())
        saveButton.pack()

    def checkResults(self):
        self.endTime = time.time()
        self.done.destroy()
        timeLabel = tk.Label(self, text = f'Attempt took {time.strftime("%H:%M:%S", time.gmtime(self.endTime - self.startTime))}', font=self.text_font)
        timeLabel.pack()
        self.csv_file.append(timeLabel.cget("text"))
        self.userAccuracy()

    def save(self):
        with open("file.txt","a") as file:
            file.write("\n")
            for item in self.csv_file:
                help = item + " "
                file.write(f'{help}')
            file.write("\n")

def main():
    one = gui()
    two = gui()
    three = gui()

if __name__ == '__main__':    
    main()