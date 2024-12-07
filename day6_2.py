import copy

input = open('input_day6.txt', 'r')

matrix = []

line = input.readline()

while line:
    newRow = [char for char in line]

    matrix.append(newRow)

    line = input.readline()

workpos = {}

for y, row in enumerate(matrix):
    for x, byte in enumerate(matrix[y]):
        if byte == '^':
            workpos[0] = x
            workpos[1] = y
            print(f"{x},{y}")
            break
    
    if len(workpos) > 0:
        break

def setObstruction():
    global matrix
    global direction
    global workpos
    global alldone

    originalChar = ''

    temppos = {0: workpos[0], 1: workpos[1]}

    if direction == 'u':
        temppos[1] -= 1
        if temppos[1] >= 0:
            if matrix[temppos[1]][temppos[0]] == '#':
                temppos[1] += 1
                direction = 'r'
            else:
                originalChar = matrix[temppos[1]][temppos[0]]
                matrix[temppos[1]][temppos[0]] = 'O'
        else:
            alldone = True
    elif direction == 'd':
        temppos[1] += 1
        if temppos[1] < len(matrix):
            if matrix[temppos[1]][temppos[0]] == '#':
                temppos[1] -= 1
                direction = 'l'
            else:
                originalChar = matrix[temppos[1]][temppos[0]]
                matrix[temppos[1]][temppos[0]] = 'O'
        else:
            alldone = True
    elif direction == 'l':
        temppos[0] -= 1
        if temppos[0] >= 0:
            if matrix[temppos[1]][temppos[0]] == '#':
                temppos[0] += 1
                direction = 'u'
            else:
                originalChar = matrix[temppos[1]][temppos[0]]
                matrix[temppos[1]][temppos[0]] = 'O'
        else:
            alldone = True
    elif direction == 'r':
        temppos[0] += 1
        if temppos[0] < len(matrix[temppos[1]]):
            if matrix[temppos[1]][temppos[0]] == '#':
                temppos[0] -= 1
                direction = 'd'
            else:
                originalChar = matrix[temppos[1]][temppos[0]]
                matrix[temppos[1]][temppos[0]] = 'O'
        else:
            alldone = True

    return originalChar

def resetObstruction(resetTo):
    global matrix
    global direction
    global workpos

    if direction == 'u':
        workpos[1] -= 1
        if matrix[workpos[1]][workpos[0]] == '#':
            workpos[1] += 1
            direction = 'r'
        else:
            matrix[workpos[1]][workpos[0]] = resetTo
    elif direction == 'd':
        workpos[1] += 1
        if matrix[workpos[1]][workpos[0]] == '#':
            workpos[1] -= 1
            direction = 'l'
        else:
            matrix[workpos[1]][workpos[0]] = resetTo
    elif direction == 'l':
        workpos[0] -= 1
        if matrix[workpos[1]][workpos[0]] == '#':
            workpos[0] += 1
            direction = 'u'
        else:
            matrix[workpos[1]][workpos[0]] = resetTo
    elif direction == 'r':
        workpos[0] += 1
        if matrix[workpos[1]][workpos[0]] == '#':
            workpos[0] -= 1
            direction = 'd'
        else:
            matrix[workpos[1]][workpos[0]] = resetTo

    return

def move():
    global matrix
    global direction
    global workpos
    global done

    if direction == 'u':
        workpos[1] -= 1
        while workpos[1] >= 0:
            if matrix[workpos[1]][workpos[0]] == '#' or matrix[workpos[1]][workpos[0]] == 'O':
                workpos[1] += 1
                direction = 'r'
                break
            if matrix[workpos[1]][workpos[0]] == direction:
                break
            matrix[workpos[1]][workpos[0]] = direction
            workpos[1] -= 1
        if workpos[1] < 0:
            done = True
    elif direction == 'd':
        workpos[1] += 1
        while workpos[1] < len(matrix):
            if matrix[workpos[1]][workpos[0]] == '#' or matrix[workpos[1]][workpos[0]] == 'O':
                workpos[1] -= 1
                direction = 'l'
                break
            if matrix[workpos[1]][workpos[0]] == direction:
                break
            matrix[workpos[1]][workpos[0]] = direction
            workpos[1] += 1
        if workpos[1] >= len(matrix):
            done = True
    elif direction == 'l':
        workpos[0] -= 1
        while workpos[0] >= 0:
            if matrix[workpos[1]][workpos[0]] == '#' or matrix[workpos[1]][workpos[0]] == 'O':
                workpos[0] += 1
                direction = 'u'
                break
            if matrix[workpos[1]][workpos[0]] == direction:
                break
            matrix[workpos[1]][workpos[0]] = direction
            workpos[0] -= 1
        if workpos[0] < 0:
            done = True
    elif direction == 'r':
        workpos[0] += 1
        while workpos[0] < len(matrix[workpos[1]]):
            if matrix[workpos[1]][workpos[0]] == '#' or matrix[workpos[1]][workpos[0]] == 'O':
                workpos[0] -= 1
                direction = 'd'
                break
            if matrix[workpos[1]][workpos[0]] == direction:
                break
            matrix[workpos[1]][workpos[0]] = direction
            workpos[0] += 1
        if workpos[0] >= len(matrix[workpos[1]]):
            done = True

    return

alldone = False

obstructions = 0

direction = 'u'

while not alldone:
    done = False

    savepos = {0: workpos[0], 1: workpos[1]}
    savedir = direction

    originalChar = setObstruction()

    savematrix = copy.deepcopy(matrix)

    while not done:
        move()

        if not done:
            if workpos[0] == savepos[0] and workpos[1] == savepos[1] and direction == savedir:
                break
        
            if matrix[workpos[1]][workpos[0]] == direction:
                break

    matrix = copy.deepcopy(savematrix)

    workpos = {0: savepos[0], 1: savepos[1]}
    direction = savedir

    if done:
        resetObstruction('X')
    else:
        if originalChar == '.':
            obstructions += 1
        resetObstruction('Y')

print(f"Obstructions: {obstructions}")