'''
Program: Term Programming Project #1
Author: Maria Viveros
Date: 10/04/2021
Purpose: Write a program that receives a series of numbers from the user and allows the user 
to press the enter key to indicate that he or she is finished providing inputs. 
After the user presses the enter key, the program should print the sum of the numbers and their average.
'''

import math

theSum = 0.0
count = 0

while True:
    data = input("Enter a number, or press enter if you are finished: ")
    
    if data == "":
     break
 
    num = float(data)
    theSum += num
    count += 1

avg = theSum / count

print("The sum of the numbers is: ", theSum)
print("The average of the numbers is: ", avg)

