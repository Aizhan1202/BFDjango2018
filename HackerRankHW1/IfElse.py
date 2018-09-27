#!/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
if(N % 2 == 1):
    print ("Weird")
elif (N % 2 == 0 and N >= 2 and N <= 5):
    print ("Not Weird")
elif (N % 2 == 0 and N >= 6 and N <= 20):
    print ("Weird")
elif (N % 2 == 0 and N > 20):
    print ("Not Weird")


