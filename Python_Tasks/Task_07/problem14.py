# Problem 14 : Anagram
# HackerRank Link : https://www.hackerrank.com/challenges/anagram/problem


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]

    count1 = Counter(s1)
    count2 = Counter(s2)

    changes = 0

    for char in count1:
        if count1[char] > count2[char]:
            changes += count1[char] - count2[char]

    return changes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input().strip()
        result = anagram(s)
        fptr.write(str(result) + '\n')

    fptr.close()
