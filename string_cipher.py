''' 
Program: 20211024
Author: Maria Viveros
Date: 10/04/2021
Purpose: Illustrate string usage, cipher coding and file access
'''

import math

# create a string implicitly

s = 'Maria Jose Viveros'

print("Length of string: ", len(s))

# create a list

l = ["Maria","Jose","Viveros"]

#print("The object id of l is: ", id(l))

for s1 in l:
	print(s1)
	
# now exercise some string handling operators and functions

# print a character by index in a string

print ("print the 5 character in s: ", s[4])

# print a character based on a negative index
print ("print a character in s, -2 places from the end of string: ", s[-4])

# lets look at a range

print("print a range in s: ", s[0:8])

# lets test the "in" operator

print("is 'iver' in s: ", "iver" in s)


