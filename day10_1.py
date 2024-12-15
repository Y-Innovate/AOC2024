input = open('input_day10.txt', 'r')

matrix = []

line = input.readline()

while line:
    newRow = line.encode()

    matrix.append(newRow)

    line = input.readline()

class Nine:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"New nine {x}, {y}")

class TrailHead:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nines = []
    
    def count(self):
        self.walk(self.x, self.y)
    
    def walk(self, x, y):
        thisChar = matrix[y][x]

        if thisChar == 57:
            found = False

            for nine in self.nines:
                if nine.x == x and nine.y == y:
                    found = True
                    break
            
            if not found:
                newNine = Nine(x, y)

                self.nines.append(newNine)

        else:
            if y > 0:
                charUp = matrix[y - 1][x]

                if charUp == thisChar + 1:
                    self.walk(x, y - 1)
            
            if x < len(matrix[y]) - 2:
                charRight = matrix[y][x + 1]

                if charRight == thisChar + 1:
                    self.walk(x + 1, y)
            
            if y < len(matrix) - 1:
                charDown = matrix[y + 1][x]

                if charDown == thisChar + 1:
                    self.walk(x, y + 1)
            
            if x > 0:
                charLeft = matrix[y][x - 1]

                if charLeft == thisChar + 1:
                    self.walk(x - 1, y)

trailHeads = []

def countTrails(x, y):
    global matrix
    global trailHeads

    newTrailHead = TrailHead(x, y)

    trailHeads.append(newTrailHead)

    newTrailHead.count()

for y in range(0, len(matrix)):
    for x in range(0, len(matrix[y]) - 1):
        if matrix[y][x] == 48:
            countTrails(x, y)

total = 0

for trailHead in trailHeads:
    total += len(trailHead.nines)

print(f"Total: {total}")