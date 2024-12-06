### Imports
import sys
from aoctools import *
import re
import numpy as np
debug = False

def readfile(file):
    with open(file) as f:
        return f.readlines()
    
def splitlines(lines, delim):
    out = []
    for line in lines:
        line = re.sub('\n', '', line)
        line = line.split(delim)
        line = list(map(int, line))
        out.append(line)
    return out

def ruledetect(list1, list2):
    for val in list1:
        if val in list2:
            return True
    return False

def rules_check (rules, manual):
    rule_res = []
    violated_rules = []
    for  rule in rules:
        rule_present = all(map(lambda v: v in manual, rule))
        if rule_present:
            if re.findall(f'{rule[1]}.*{rule[0]}', str(manual)) != []:
                rule_pass = False
                violated_rules.append(rule)
            else:
                rule_pass = True
            rule_res.append(rule_pass)
    return min(rule_res) == True, violated_rules

rules = readfile('./data/input_day_5_rules.txt')
rules = splitlines(rules, '|')
manuals = readfile('./data/input_day_5_manuals.txt')
manuals = splitlines(manuals, ',')


ans=0



good_list = [69, 17, 83]
bad_list = [17, 69, 83]


for manual in manuals:
    passed, failed_rules = rules_check(rules, manual)
    if passed:
        middle_index = int((len(manual)-1)/2)
        # print(manual,  manual[middle_index])
        ans += manual[middle_index]
    else:
        if debug:
            print(failed_rules, manual)
        pass

print(f'\nTodays answer is: {ans}\n')
    


