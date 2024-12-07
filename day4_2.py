input = open('input_day4.txt', 'r')

matrix = []

line = input.readline()

while line:
    newRow = line.encode()

    matrix.append(newRow)

    line = input.readline()

def check(c1, c3):
    itsXMAS = False

    if matrix[c1[1]][c1[0]] == 77 and \
       matrix[c3[1]][c3[0]] == 83:
        itsXMAS = True
    
    return itsXMAS

def isItXMASYet(x, y):
    xcount = 0

    if check((x - 1, y - 1), (x + 1, y + 1)):
        xcount += 1

    if check((x + 1, y - 1), (x - 1, y + 1)):
        xcount += 1

    if check((x - 1, y + 1), (x + 1, y - 1)):
        xcount += 1
    
    if check((x + 1, y + 1), (x - 1, y - 1)):
        xcount += 1

    return xcount

count = 0

for y, row in enumerate(matrix):
    for x, col in enumerate(matrix[y]):
        if x > 0 and x < len(matrix[y]) - 1 and \
           y > 0 and y < len(matrix) - 1 and \
           matrix[y][x] == 65:
            addCount = isItXMASYet(x, y)

            if addCount > 1:
                count += 1

print(f"Total: {count}")