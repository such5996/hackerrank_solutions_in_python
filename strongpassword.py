#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    c = 0
    l = u = num = ch = r = b = 0
    if (n < 6):
        for char in password:
            if(char.islower()):
                l = 1
            if(char.isupper()):
                u = 1
            if(char.isnumeric()):
                num = 1
            if(char in ['!','@','#','$','%','^','&','*','(',')','-','+']):
                ch = 1
            
        r = max((4 - (ch+l+u+num)), 6 - n)
        return r
        
    elif(n>=6 and n<=100):
        for char in password:
            if(char.islower() == True):
                l = 1
            if(char.isupper() == True):
                u = 1
            if(char.isnumeric() == True):
                num = 1
            if(char in ['!','@','#','$','%','^','&','*','(',')','-','+']):
                ch = 1
        b = 4 - (ch+u+l+num)
        return b
                

                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
