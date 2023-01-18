'''
Program: Fall back program for today
Author: Maria Viveros
Date: 09/20/21
Purpose: Illustrate modules and structures
'''

import random

#show contents of imported module, random

#print(dir(random))

#print(help(random.randint))

#first implement a fixed iteration loop

for i in range(1, 4):
	print(" %2d " % random.randint(1,6))
	
#generate 10 random ints only print if odd

for i in range(0,10):
	rn = random.randint(1,32767)
	
	if (rn % 2) == 1:
		if rn >16000:
			print(' %2d ' % rn)
