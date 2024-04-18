# from time import time
import time
import random
import tkinter as tk
from csv import *

class gui(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("800x700+400+200") # Horizontal x Vertical
        self.minsize(800, 700)
        self.maxsize(1500, 800)
        self.title("Typing Test")
        self.config(padx=50, pady=10)
        self.instructions = tk.Label(wraplength=700, justify='center',font=('Arial', 14), text = "Type the prompt. The timer starts at the first keystroke. To end the typing portion, use the mouse to hit done. The QB test will then start.") 
        self.instructions.pack() # add the label to the window

        self.file = tk.Button(self, text = "Get the Typing Test", command=self.getFile)
        self.file.pack()

        # self.start = tk.Button(self, text = "Start", command=self.startUserInput)
        # self.start.pack(side = "bottom", padx=10, pady=5)

        self.typingWindow = tk.Frame(width=200, height=40, padx=5, pady=5)
        # self.typingWindow.place(x=100, y = 100)
        self.typingWindow.pack(side = 'bottom')

        self.typingArea = tk.Text(self.typingWindow, wrap='w', padx=5, pady=5, fg='black', bg='white', font='14')
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
        label = tk.Label(self, text=original, font=('Arial', 14))
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
            accuracyLabel = tk.Label(self, text = f'{self.accuracy:.3}% accuracy', font=('Arial', 20))
            # accuracyText = "accuracy"
            self.csv_file.append(accuracyLabel.cget("text"))
        else:
            accuracyLabel = tk.Label(self, text = f'{self.accuracy}% accuracy', font=('Arial', 20))
            self.csv_file.append(accuracyLabel.cget("text"))
        accuracyLabel.pack()
        self.typingArea.destroy()
        print(self.csv_file)
        saveButton = tk.Button(self,text="Save", command=self.save())
        saveButton.pack()

    def checkResults(self):
        self.endTime = time.time()
        self.done.destroy()
        timeLabel = tk.Label(self, text = f'Attempt took {time.strftime("%H:%M:%S", time.gmtime(self.endTime - self.startTime))}', font=('Arial', 20))
        timeLabel.pack()
        self.csv_file.append(timeLabel.cget("text"))
        self.userAccuracy()

    def save(self):
        with open("file.txt","a") as file:
            Writer=writer(file)
            Writer.writerow(["accuracy","time"])
            Writer.writerows(self.csv_file)
            self.remove_commas()

    def remove_commas(self):
        with open("file.txt", "r") as file:
            commas = file.readlines()
        with open("file.txt", "w") as file:
            for c in commas:
                c.strip(",")
                file.write(c)

def main():
    one = gui()
    # one.mainloop()

if __name__ == '__main__':    
    main()