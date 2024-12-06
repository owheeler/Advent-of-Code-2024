### Imports
import sys
from aoctools import *
import re


with open('./data/input_day_3.txt') as f:
    lines = f.readlines()
# part1
ans=0

def findall(l):
    res = []
    for l in l:
        res.extend(re.findall("mul\([0-9]{1,3}\,[0-9]{1,3}\)", l))
    return res

out = findall(lines)

for tuple in out:
    print(tuple)
    ls = re.findall("[0-9]{1,3}", str(tuple))
    print(ls)
    ans += int(ls[0])*int(ls[1])

print(f'Part 1 answer: {ans}\n')

# part 2
pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, open("./data/input_day_3.txt").read())

ans = 0
flag = True
print(matches)
for match in matches:
    if match == "do()":
        flag = True
    elif match == "don't()":
        flag = False
    else:
        if flag:
            x,y = map(int, match[4:-1].split(","))
            ans += x*y



print(f'Part 2 answer: {ans}\n')