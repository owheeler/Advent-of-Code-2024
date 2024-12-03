### Imports
import re

## Part 1 Code

with open('./data/input_day_1.txt') as f:
    lines = f.readlines()

# Read into two separate lists
col1 = []
col2 = []
for line in lines:
    line = re.sub("[^0-9]", '', line)
    left = int(line[:5])
    right = int(line[-5:])
    col1.append(left)
    col2.append(right)

# Sort the lists
col1.sort()
col2.sort()

distances = [abs(a-b) for a,b in zip(col1,col2)]

print(f'Part 1 result: {sum(distances)}\n')


## Part 2 code
similarity = []
for i, val in enumerate(col1):
    matches = col2.count(val)
    valsimilarity = val*matches
    similarity.append(valsimilarity)

print(f'Part 2 similarity: {sum(similarity)}\n')