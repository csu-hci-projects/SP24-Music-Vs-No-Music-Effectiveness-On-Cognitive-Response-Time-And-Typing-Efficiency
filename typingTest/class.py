# from time import time
import time
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
        self.instructions = tk.Label(text = "Type the prompt. The timer start at the first keystroke. To end the timer, use the mouse to hit the text box.") 
        self.instructions.pack() # add the label to the window

        self.file = tk.Button(self, text = "Get the Typing Test", command=self.getFile)
        self.file.pack()

        # self.start = tk.Button(self, text = "Start", command=self.startUserInput)
        # self.start.pack(side = "bottom", padx=10, pady=5)

        self.typingWindow = tk.Frame(width=200, height=40, padx=5, pady=5)
        # self.typingWindow.place(x=100, y = 100)
        self.typingWindow.pack(side = 'bottom')

        self.typingArea = tk.Text(self.typingWindow, wrap='w', padx=5, pady=5, fg='green', bg='black')
        self.typingArea.pack()

        self.done = tk.Button(self, text='Done', command=self.checkResults)

        self.song = ""
        self.inputWords = []
        self.inputFromUser = []
        self.totalWords = len(self.inputWords)
        self.startTime = 0
        self.endTime = 0
        self.accuracy = 0


        self.mainloop()

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
        with open(fileName, 'r') as file:
            original = file.read()
            self.song = original
            self.inputWords = original.split()
            self.totalWords = len(self.inputWords)
        label = tk.Label(self, text=original)
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
        self.accuracy = sum(100 for x,y in zip(self.inputWords, self.inputFromUser) if x ==y) / self.totalWords
        print(f'{self.accuracy:.3} accuracy')

    def checkResults(self):
        self.endTime = time.time()
        self.done.destroy()
        print("Attempt took",time.strftime("%H:%M:%S", time.gmtime(self.endTime - self.startTime)))
        self.userAccuracy()

def main():
    one = gui()
    # one.mainloop()

if __name__ == '__main__':    
    main()