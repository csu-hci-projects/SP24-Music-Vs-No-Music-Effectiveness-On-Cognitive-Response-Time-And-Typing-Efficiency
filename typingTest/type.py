from time import time
import random

def wordBank():
    one = "typingTest/lovestory"
    two = "typingTest/dontstopbelievin"
    three = "typingTest/yesterday"
    four = "typingTest/beforehecheats"
    five = "typingTest/hundredyears"

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