#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(strr, n, k):
    # Write your code here
    strr = list(strr)
    palin = strr[::]

    l = 0
    r = len(strr) - 1
 
    # first try to make palindrome
    while (l <= r):
        if (strr[l] != strr[r]):
            palin[l] = palin[r] = max(strr[l], strr[r])
            k -= 1
        l += 1
        r -= 1
    if (k < 0):
        return "-1"
 
    l = 0
    r = len(strr) - 1
 
    while (l <= r):
        if (l == r):
            if (k > 0):
                palin[l] = '9'
        if (palin[l] < '9'):
 
            if (k >= 2 and palin[l] == strr[l] and palin[r] == strr[r]):
                k -= 2
                palin[l] = palin[r] = '9'
            elif (k >= 1 and (palin[l] != strr[l] or
                              palin[r] != strr[r])):
                k -= 1
                palin[l] = palin[r] = '9'
 
        l += 1
        r -= 1
    palin = str("".join(palin))            
    return palin

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
