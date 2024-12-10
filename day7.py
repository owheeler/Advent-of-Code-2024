### Imports
import sys
from aoctools import *
import re
import numpy as np
from functions import readfile
debug = True

eqs = readfile('./data/input_day_7.txt')

ans = 0

target = int(re.sub(':', '', re.match('[0-9]*:', eqs[0]).group(0)))

print(target)
print(eqs[0])
