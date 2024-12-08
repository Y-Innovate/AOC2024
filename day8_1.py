import copy

input = open('input_day8.txt', 'r')

matrix = []

line = input.readline()

while line:
    newRow = [char for char in line]

    newRow.pop()

    matrix.append(newRow)

    line = input.readline()

matrix2 = copy.deepcopy(matrix)

sizX = len(matrix[0])
sizY = len(matrix)

def findAll(toCheck):
    global matrix

    found = []

    for y, row in enumerate(matrix):
        for x, col in enumerate(matrix[y]):
            if matrix[y][x] == toCheck:
                found.append([x, y])
    
    return found

uniqueAntinodes = 0

allToCheck = "abcdefghijklmnopqrstuvwxyz"
allToCheck = allToCheck + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
allToCheck = allToCheck + "0123456789"

for idxToCheck in range(0, len(allToCheck)):
    toCheck = allToCheck[idxToCheck]

    found = findAll(toCheck)

    for idx1 in range(0, len(found) - 1):
        for idx2 in range(idx1 + 1, len(found)):
            deltaX = found[idx2][0] - found[idx1][0]
            deltaY = found[idx2][1] - found[idx1][1]

            antinode1 = [found[idx1][0] - deltaX, found[idx1][1] - deltaY]
            antinode2 = [found[idx2][0] + deltaX, found[idx2][1] + deltaY]

            if antinode1[0] >= 0 and antinode1[0] < sizX and \
               antinode1[1] >= 0 and antinode1[1] < sizY:
                if matrix2[antinode1[1]][antinode1[0]] != '#':
                    uniqueAntinodes += 1
                    matrix2[antinode1[1]][antinode1[0]] = '#'

            if antinode2[0] >= 0 and antinode2[0] < sizX and \
               antinode2[1] >= 0 and antinode2[1] < sizY:
                if matrix2[antinode2[1]][antinode2[0]] != '#':
                    uniqueAntinodes += 1
                    matrix2[antinode2[1]][antinode2[0]] = '#'

print(f"Antinodes: {uniqueAntinodes}")