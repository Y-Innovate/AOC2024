input = open('input_day4.txt', 'r')

matrix = []

line = input.readline()

while line:
    newRow = line.encode()

    matrix.append(newRow)

    line = input.readline()

def check(c2, c3, c4):
    itsXMAS = False

    if matrix[c2[1]][c2[0]] == 77 and \
       matrix[c3[1]][c3[0]] == 65 and \
       matrix[c4[1]][c4[0]] == 83:
        itsXMAS = True
    
    return itsXMAS

def isItXMASYet(x, y):
    xcount = 0

    # horizontal to the right
    if x <= len(matrix[y]) - 4:
        if check((x + 1, y), (x + 2, y), (x + 3, y)):
            xcount += 1

        # diagonal right and down        
        if y <= len(matrix) - 4:
            if check((x + 1, y + 1), (x + 2, y + 2), (x + 3, y + 3)):
                xcount += 1
        
        # diagonal right and up
        if y >= 3:
            if check((x + 1, y - 1), (x + 2, y - 2), (x + 3, y - 3)):
                xcount += 1
    
    # horizontal to the left
    if x >= 3:
        if check((x - 1, y), (x - 2, y), (x - 3, y)):
            xcount += 1
        
        # diagonal left and down
        if y <= len(matrix) - 4:
            if check((x - 1, y + 1), (x - 2, y + 2), (x - 3, y + 3)):
                xcount += 1
        
        # diagonal left and up
        if y >= 3:
            if check((x - 1, y - 1), (x - 2, y - 2), (x - 3, y - 3)):
                xcount += 1
    
    # vertical down
    if y <= len(matrix) - 4:
        if check((x, y + 1), (x, y + 2), (x, y + 3)):
            xcount += 1
    
    # vertical up
    if y >= 3:
        if check((x, y - 1), (x, y - 2), (x, y - 3)):
            xcount += 1

    return xcount

count = 0

for y, row in enumerate(matrix):
    for x, col in enumerate(matrix[y]):
        if matrix[y][x] == 88:
            addCount = isItXMASYet(x, y)

            count += addCount

print(f"Total: {count}")