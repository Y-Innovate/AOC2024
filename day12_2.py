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
idmatrix = copy.deepcopy(matrix)

regionid = 0

class Plot:
    def __init__(self, x, y, regionid):
        global workmatrix
        global idmatrix

        self.x = x
        self.y = y
        self.regionid = regionid
        self.fenceCount = 0
        self.corner = False

        workmatrix[y][x] = 0
        idmatrix[y][x] = regionid

class Region:
    def __init__(self, x, y):
        global matrix
        global regionid

        regionid += 1
        self.regionid = regionid

        self.x = x
        self.y = y
        self.minx = x
        self.maxx = x
        self.miny = y
        self.maxy = y
        self.id = matrix[y][x]
        self.plots = []
        self.fenceCount = 0

    def fenceRegion(self):
        self.findPlots(self.x, self.y)

        for plot in self.plots:
            corner = 0
            if plot.y == 0 or matrix[plot.y - 1][plot.x] != self.id:
                plot.fenceCount += 1
                corner += 1
            if plot.y >= len(matrix) - 1 or matrix[plot.y + 1][plot.x] != self.id:
                plot.fenceCount += 1
                corner += 1
            if plot.x == 0 or matrix[plot.y][plot.x - 1] != self.id:
                plot.fenceCount += 1
                corner -= 1
            if plot.x >= len(matrix[y]) - 1 or matrix[plot.y][plot.x + 1] != self.id:
                plot.fenceCount += 1
                corner -= 1
            
            self.fenceCount += plot.fenceCount

            if plot.fenceCount == 2 and corner == 0:
                plot.corner = True

    def findPlots(self, x, y):
        global matrix
        global workmatrix

        somePlot = Plot(x, y, self.regionid)

        self.addPlot(somePlot)

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
    
    def addPlot(self, somePlot):
        if somePlot.x < self.minx:
            self.minx = somePlot.x
        if somePlot.x > self.maxx:
            self.maxx = somePlot.x
        if somePlot.y < self.miny:
            self.miny = somePlot.y
        if somePlot.y > self.maxy:
            self.maxy = somePlot.y

        self.plots.append(somePlot)

regions = []

for y in range(0, len(matrix)):
    for x in range(0, len(matrix[y])):
        if workmatrix[y][x] != 0:
            someRegion = Region(x, y)

            someRegion.fenceRegion()

            regions.append(someRegion)

totalprice = 0

for region in regions:

    if len(region.plots) == 1:
        totalprice += 4
    else:
        if region.minx == region.maxx or region.miny == region.maxy:
            totalprice += len(region.plots) * 4
        else:
            corners = 0
            
            for plot in region.plots:
                if plot.fenceCount == 2 and plot.corner:
                    corners += 1
                elif plot.fenceCount == 3:
                    corners += 2

            for y in range(region.miny, region.maxy):
                for x in range(region.minx, region.maxx):
                    outOfFour = 0

                    if matrix[y][x] == region.id and idmatrix[y][x] == region.regionid:
                        outOfFour += 1
                    if matrix[y][x + 1] == region.id and idmatrix[y][x + 1] == region.regionid:
                        outOfFour += 1
                    if matrix[y + 1][x] == region.id and idmatrix[y + 1][x] == region.regionid:
                        outOfFour += 1
                    if matrix[y + 1][x + 1] == region.id and idmatrix[y + 1][x + 1] == region.regionid:
                        outOfFour += 1
                    
                    if outOfFour == 3:
                        corners += 1

            totalprice += len(region.plots) * corners

print(f"Total price: {totalprice}")