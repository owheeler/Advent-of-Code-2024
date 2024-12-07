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

def find_location(map):
    for row_num, row in enumerate(map):
            for col_num, column in enumerate(row):
                if map[row_num][col_num] in ['^', '>', 'v', '<']:
                    r = row_num
                    c = col_num
                    break
    return r, c

def move_up( map,r,c):
    direction = ''
    current_location = [r,c]
    counter = 0 
    debug = False
    while direction == '' :
        if counter > 300:
            print('too many iterations')
            break
        # Capture current location and target location
        
        current_location = [r,c]
        next_location = [r-1, c]
        
        next_location_char = map[next_location[0]][next_location[1]]
        if debug:
            print(f'Current Location: {current_location}\t checking {next_location}\t{next_location_char}')
        # Check next location and move if clear turn if not
        if next_location_char == '#':
            direction = 'right'
        else:
        # Update current and new locations
            map[current_location[0]][current_location[1]] = 'X'
            map[next_location[0]][next_location[1]] = '^'
            r = next_location[0]
            c = next_location[1]
        if r == 0 or r == 129 or c == 0 or c == 129:
            break
        counter += 1
        if debug:
            for row in map:
                print(''.join(row))
            print(direction)
    return map, direction , counter

def move_right( map,r,c):
    direction = ''
    current_location = [r,c]
    counter = 0
    while direction == '' :
        if counter > 300:
            print('too many iterations')
            break
        # Capture current location and target location
        current_location = [r,c]
        next_location = [r, c+1]
                
        # Check next location and move if clear turn if not
        if map[next_location[0]][next_location[1]] == '#':
            direction = 'down'
        else:
        # Update current and new locations
            map[current_location[0]][current_location[1]] = 'X'
            map[next_location[0]][next_location[1]] = '>'
            r = next_location[0]
            c = next_location[1]
        if r == 0 or r == 129 or c == 0 or c == 129:
            break
        counter += 1
    return map, direction , counter

def move_down( map,r,c):
    direction = ''
    current_location = [r,c]
    counter = 0
    while direction == '' :
        if counter > 300:
            print('too many iterations')
            break
        # Capture current location and target location
        current_location = [r,c]
        next_location = [r+1, c]
        
        # Check next location and move if clear turn if not
        if map[next_location[0]][next_location[1]] == '#':
            direction = 'left'
        else:
        # Update current and new locations
            map[current_location[0]][current_location[1]] = 'X'
            map[next_location[0]][next_location[1]] = 'v'
            r = next_location[0]
            c = next_location[1]
        if r == 0 or r == 129 or c == 0 or c == 129:
            break
    counter += 1
    return map, direction , counter

def move_left( map, r, c):
    direction = ''
    current_location = [r,c]
    counter = 0
    while direction == '' :
        if counter > 300:
            print('too many iterations')
            break
        # Capture current location and target location
        current_location = [r,c]
        next_location = [r, c-1]
        
        # Check next location and move if clear turn if not
        if map[next_location[0]][next_location[1]] == '#':
            direction = 'up'
        else:
        # Update current and new locations
            map[current_location[0]][current_location[1]] = 'X'
            map[next_location[0]][next_location[1]] = '<'
            r = next_location[0]
            c = next_location[1]
        if r == 0 or r == 129 or c == 0 or c == 129:
            break
    counter +=1
    return map, direction , counter


def navigation(map, direction):
    exit_criteria = False
    counter = 0
    countern = 0
    print('Starting Map')
    for row in map:
            print(''.join(row))

    while not exit_criteria and countern < 200:

        r, c = find_location(map)
        # print(r,c)
        exit_criteria = r == 0 or r == 129 or c == 0 or c == 129
        if direction == 'up':
            map, direction, counter = move_up(map, r, c)
            # for row in map:
            #     print(''.join(row))
            continue
        if direction == 'right':
            map, direction, counter = move_right(map, r, c)
            # for row in map:
            #     print(''.join(row))
            continue
        if direction == 'down':
            map, direction, counter = move_down(map,r,c)
            # for row in map:
            #     print(''.join(row))
            continue
        if direction == 'left':
            map, direction, counter = move_left(map,r,c)
            # for row in map:
            #     print(''.join(row))
            continue
        countern +=1
        # print(direction, countern, '\n\n')
    print('Final Map')
    for row in map:
        print(''.join(row))
    print(f'Final location is: [{r},{c}]')
    return map, direction

