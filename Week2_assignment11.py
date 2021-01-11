'''
In this assignment you will read through and parse a file with text and numbers.
You will extractall the numbers in the file and compute the sum of the numbers.
'''

import re
handle = open('regex_sum.txt')
numlist = list()
for line in handle:
    line = line.rstrip()
    stuff = re.findall('[0-9]+',line)
    if len(stuff)==0: continue
    for i in range(len(stuff)):
        num = int(stuff[i])
        numlist.append(num)
print(len(numlist))
print(sum(numlist))
