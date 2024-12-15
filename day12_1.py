import copy

input = open('input_day12.txt', 'r')

matrix = []

line = input.readline()

while line:
    newRow = [char for char in line]

    newRow.pop()

    matrix.append(newRow)

    line = input.readline()

workmatrix = copy.deepcopy(matrix)

class Plot:
    def __init__(self, x, y):
        global workmatrix

        self.x = x
        self.y = y
        self.fenceCount = 0

        workmatrix[y][x] = 0

class Region:
    def __init__(self, x, y):
        global matrix

        self.x = x
        self.y = y
        self.id = matrix[y][x]
        self.plots = []
        self.fenceCount = 0

    def fenceRegion(self):
        self.findPlots(self.x, self.y)

        for plot in self.plots:
            if plot.y == 0 or matrix[plot.y - 1][plot.x] != self.id:
                plot.fenceCount += 1
            if plot.y >= len(matrix) - 1 or matrix[plot.y + 1][plot.x] != self.id:
                plot.fenceCount += 1
            if plot.x == 0 or matrix[plot.y][plot.x - 1] != self.id:
                plot.fenceCount += 1
            if plot.x >= len(matrix[y]) - 1 or matrix[plot.y][plot.x + 1] != self.id:
                plot.fenceCount += 1
            
            self.fenceCount += plot.fenceCount

    def findPlots(self, x, y):
        global matrix
        global workmatrix

        somePlot = Plot(x, y)

        self.plots.append(somePlot)

        if y > 0:
            if workmatrix[y - 1][x] == self.id:
                self.findPlots(x, y - 1)
        if y < len(matrix) - 1:
            if workmatrix[y + 1][x] == self.id:
                self.findPlots(x, y + 1)
        if x > 0:
            if workmatrix[y][x - 1] == self.id:
                self.findPlots(x - 1, y)
        if x < len(matrix[y]) - 1:
            if workmatrix[y][x + 1] == self.id:
                self.findPlots(x + 1, y)

regions = []

for y in range(0, len(matrix)):
    for x in range(0, len(matrix[y])):
        if workmatrix[y][x] != 0:
            someRegion = Region(x, y)

            someRegion.fenceRegion()

            regions.append(someRegion)

totalprice = 0

for region in regions:
    totalprice += len(region.plots) * region.fenceCount

print(f"Total price: {totalprice}")