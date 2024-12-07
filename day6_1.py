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

def move():
    global matrix
    global direction
    global workpos
    global done

    count = 0

    if direction == 'u':
        workpos[1] -= 1
        while workpos[1] >= 0:
            if matrix[workpos[1]][workpos[0]] == '#':
                workpos[1] += 1
                direction = 'r'
                break
            elif matrix[workpos[1]][workpos[0]] == '.':
                count += 1
                matrix[workpos[1]][workpos[0]] = 'X'
            workpos[1] -= 1
        if workpos[1] < 0:
            done = True
    elif direction == 'd':
        workpos[1] += 1
        while workpos[1] < len(matrix):
            if matrix[workpos[1]][workpos[0]] == '#':
                workpos[1] -= 1
                direction = 'l'
                break
            elif matrix[workpos[1]][workpos[0]] == '.':
                count += 1
                matrix[workpos[1]][workpos[0]] = 'X'
            workpos[1] += 1
        if workpos[1] >= len(matrix):
            done = True
    elif direction == 'l':
        workpos[0] -= 1
        while workpos[0] >= 0:
            if matrix[workpos[1]][workpos[0]] == '#':
                workpos[0] += 1
                direction = 'u'
                break
            elif matrix[workpos[1]][workpos[0]] == '.':
                count += 1
                matrix[workpos[1]][workpos[0]] = 'X'
            workpos[0] -= 1
        if workpos[0] < 0:
            done = True
    elif direction == 'r':
        workpos[0] += 1
        while workpos[0] < len(matrix[workpos[1]]):
            if matrix[workpos[1]][workpos[0]] == '#':
                workpos[0] -= 1
                direction = 'd'
                break
            elif matrix[workpos[1]][workpos[0]] == '.':
                count += 1
                matrix[workpos[1]][workpos[0]] = 'X'
            workpos[0] += 1
        if workpos[0] >= len(matrix[workpos[1]]):
            done = True

    return count    

done = False

distrinctPositions = 1

direction = 'u'

while not done:
    addCount = move()

    distrinctPositions += addCount

print(f"Distinct positions: {distrinctPositions}")