### Imports
import sys
from aoctools import *
import re
import numpy as np
from functions import readfile, navigation, find_location
debug = True

map = readfile('./data/input_day_6.txt')

mapa = []
for line in map:
    line = re.sub('\n', '', line)
    mapa.append(list(line))




starting_direction = 'up'

map, direction = navigation(mapa, starting_direction)

r,c = find_location(map)



unique, counts = np.unique(map, return_counts=True)

char_counts = dict(zip(unique, counts))

ans = char_counts['X']+ 1

print(f'\nTodays answer is: {ans}\n')
    


