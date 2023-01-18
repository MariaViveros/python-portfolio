'''
Program: Term Programming Project #3
Author: Maria Viveros
Date: 11/18/21
Purpose: Write a GUI-based program that plays a guess-the-number game. The computer guesses a 
number between 1 and 100 and the user provides the responses.The user enters a hint in response.

'''
import random
from breezypythongui import EasyFrame
 
class GuessingGame(EasyFrame):
     """Plays a guessing game with the user."""
    def __init__(self):
        """Sets up the window, widgets, and data."""
        EasyFrame.__init__(self, title = "Guessing Game")
        # Initialize the instance variables for the data
        self.guessNumber = random.randint(1, 100)
        self.count = 0
        # Create and add widgets to the window
        greeting = "Think a number between 1 and 100, and let me guess it."
        self.startLabel = self.addLabel(text = greeting,
                                         row = 0, column = 0,
                                         sticky = "NSEW",
                                         columnspan = 2)
        self.smallButton = self.addButton(text = "Too small", row = 3,
                                           column = 0, command = self.tooSmall)
        self.largeButton = self.addButton(text = "Too large", row = 3,
                                           column = 1, command = self.tooLarge) 
        self.correctButton = self.addButton(text = "Correct", row = 3,
                                           column = 2, command = self.Correct)                                   
         
        self.newButton = self.addButton(text = "New game",
                                           row = 4, column = 1, command = self.nextGuess)
                                               
    def tooSmall(self):
        self.count += 1
        self.guessNumber = random.randint(self.guessNumber, 100)
        self.startLabel["text"] =  "Is it" + str(self.guessNumber) + "?"
        
    def tooLarge(self): 
        self.count += 1
        self.guessNumber = random.randint(1, self.guessNumber)
        self.startLabel["text"] =  "Is it" + str(self.guessNumber) + "?"
        
    def Correct(self):   
        self.smallButton["state"] = "disabled"
        self.largeButton["state"] = "disabled"
        self.correctButton["state"] = "disabled"
        self.startLabel["text"] = "I did it in " + str(self.count) + " attempts!"
             
    def newGame(self):
        self.guessNumber = random.randint(1, 100)
        self.count = 0
        greeting = "Think a number between 1 and 100. Is it" + str(self.guessNumber) + "?"
        self.startLabel["text"] = greeting
     
def main():
     GuessingGame().mainloop()
     
if __name__ == "__main__":
     main()  