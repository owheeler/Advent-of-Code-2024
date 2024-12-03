### Imports
import re

## Part 1 Code

with open('./data/input_day_2.txt') as f:
    lines = f.readlines()


def counttrues(lst):
 
    return sum(bool(x) for x in lst)


fails = 0
debug = False

for row, line in enumerate(lines):
    result = True
    line_test = []
    line_split = line.split(' ')
    line_split = [int(re.sub(r'\W', '', i)) for i in line_split]
    diffs = []
    for i, val in enumerate(line_split):
        if i == 0: 
            continue
        else:
            diffs.append(line_split[i] - line_split[i-1])
    
    # Check 1:
    # No values are 0
    zeroes = [i == 0 for i in diffs]
    if counttrues(zeroes) > 0:
        result = False


    # Check 2:
    # All tests are either increasing or decreasing
    
    if diffs[0] > 0:
        if any(i < 0 for i in diffs):
            result = False

    if diffs[0] < 0:
        if any(i > 0 for i in diffs):
            result = False

    # Check 3:
    # All diffs between 1 and 3
    range = [abs(i) > 3 for i in diffs]
    if counttrues(range) > 0:
        result = False

    if not result:
        if debug:
            print('\n', row)
            print(line_split)
            print(diffs)
        fails += 1

print(f'Part 1 solution: {len(lines)-fails}')