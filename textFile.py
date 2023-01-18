'''
Program: Term Programming Project #2
Author: Maria Viveros
Date: 10/15/2021
Purpose: Read a text file, input the lines of text on it,
prompts the user for a line number, and print the line
associated with that number.
'''
        
fileName = input("Enter the file name: ")
f = open(fileName, 'r')

linecount = 0

for line in f:
    linecount = linecount + 1
print("The number of lines in this file is ", linecount)

linenum = 0

while True:
    num = int(input("Enter a line number or press 0 to quit: "))
    if num >=1 and num <= linecount:
        file = open(fileName, 'r')
        for lines in file:
            linenum = linenum + 1
            if linenum == num:
                print(lines)
    else:
        if num == 0:
            break