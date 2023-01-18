'''
Program: An excercise implementing logic structures in Python
Author: Maria Viveros
Date: 09/13/2021
Purpose: Demonstration through text of the implementation of selection and 
repetition logic structures in Python. Numeric data and strings also covered.
'''

import math
import random

#Lets look at some data types

#Lets first deal with string types

# myStr = 'Allan is wonderful'

# print(myStr)

#Lets now look at integers

# myIntStr = '15'

# myInt = int(myIntStr)

# print(myIntStr, myInt)

#Now lets look at floats

# myFloat = 3.4

# print(myFloat)

#Lets implement a simple for loop to show numeric to character conversion

# for ch in range(53,72):
#	print(ch, chr(ch))
	
#Lets implement a for loop using a smaller range

for i in 'ABCDEFGHIJKLMNOP':
	print (i,ord(i))
	
#Lets put together a bogus statement

r = -1 / 6 + 10**2 + 5 - 3 * 21 % 9 // 3

print(r) 
