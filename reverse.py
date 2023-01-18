'''
Program: Term Programming Project #5
Author: Maria Viveros
Date: 12/10/21
Purpose: Define a function named reverse that reverses the elements 
in its list argument.

'''

def reverse(lyst):
   for i in range(len(lyst)//2):
       lyst[i], lyst[len(lyst) - i - 1] =lyst[len(lyst) - i - 1], lyst[i]
       
def main():
   list1 = list(range(8))
   print("list: ",list1)

   reverse(list1)
   print("reversed list: ",list1)
   
main()