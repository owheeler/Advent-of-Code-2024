### Imports
import sys
from aoctools import *
import re

## Part 1 Code

with open('./data/input_day_2.txt') as f:
    lines = f.readlines()

ans = 0
def check(line_split):
    g = all(a > b for a,b in zip(line_split, line_split[1:])) or all(a < b for a,b in zip(line_split, line_split[1:]))
    if g:
        line_split.sort()
        for a,b in zip(line_split, line_split[1:]):
            if b - a >3 or b - a < 1:
                g = False
                break

    return g


        
for l in lines:
    line_split = l.split(' ')
    line_split = [int(re.sub(r'\W', '', i)) for i in line_split]
    if check(line_split) or any(check(line_split[:i] + line_split[i+1:]) for i in range(len(l))):
        ans += 1
print(ans)

