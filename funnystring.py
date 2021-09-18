#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    strr_ascii = []
    diff_1 =[]
    diff_2 =[]
    flag = 0
    for char in s:
        strr_ascii.append(ord(char))
    rev_ascii = strr_ascii[: :-1]
    for i in range(1,len(strr_ascii)):
        diff_1.append(abs(strr_ascii[i] - strr_ascii[i-1]))
    for i in range(1,len(rev_ascii)):
        diff_2.append(abs(rev_ascii[i] - rev_ascii[i-1]))
    
    #print(diff_1)
    #print(diff_2)
    for i in range(len(diff_1)):
        if(diff_1[i] == diff_2[i]):
            flag +=1
    
    if(flag == len(diff_1)):
        return "Funny"
    else:
        return "Not Funny"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
