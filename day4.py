### Imports
import sys
from aoctools import *
import re
import numpy as np


with open('./data/input_day_4.txt') as f:
    lines = f.readlines()
# part1


ans=0
for i, line in enumerate(lines):
    length = len(lines)
    res = re.findall('XMAS', line)
    ans += len(res) 
    res = re.findall('SAMX', line)
    ans += len(res) 

print(ans)
debug = False

for j in range(0, len(lines)):
    for k in range(0, len(lines[j])):
        if lines[j][k] == 'X' :
            # try:
            #     if (lines[j][k+1] == 'M' and lines[j][k+2] == 'A' and lines[j][k+3] == 'S'):
            #         ans+=1
            #         if debug:
            #             print(j,k, 'right')
            # except:
            #     pass
            # try:
            #     if (lines[j][k-1] == 'M' and lines[j][k-2] == 'A' and lines[j][k-3] == 'S'):
            #         ans +=1
            #         if debug:
            #             print(j,k, 'left')
            # except:
                # pass
            try:
                if (lines[j+1][k] == 'M' and lines[j+2][k] == 'A' and lines[j+3][k] == 'S'):
                    ans +=1
                    if debug:
                        print(j,k, 'down')
            except:
                pass
            try:
                if (lines[j-1][k] == 'M' and lines[j-2][k] == 'A' and lines[j-3][k] == 'S'):
                    ans +=1
                    if debug:
                        print(j,k, 'up')
            except:
                pass
            try:
                if (lines[j+1][k+1] == 'M' and lines[j+2][k+2] == 'A' and lines[j+3][k+3] == 'S'):
                    ans +=1
                    if debug:
                        print(j,k, 'down-right')
            except:
                pass
            try:
                if (lines[j+1][k-1] == 'M' and lines[j+2][k-2] == 'A' and lines[j+3][k-3] == 'S'):
                    ans +=1
                    if debug:
                        print(j,k, 'down-left')
            except:
                pass
            try:
                if (lines[j-1][k+1] == 'M' and lines[j-2][k+2] == 'A' and lines[j-3][k+3] == 'S'): 
                    ans +=1
                    if debug:
                        print(j,k, 'up-right')
            except:
                pass
            try:
                if (lines[j-1][k-1] == 'M' and lines[j-2][k-2] == 'A' and lines[j-3][k-3] == 'S'):
                    ans +=1
                    if debug:
                        print(j,k, 'up-left')
            except:
                pass

print(ans)
