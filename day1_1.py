input = open('input_day1.txt', 'r')

leftNrs = []
rightNrs = []

def insertNumber(arr, nr):
    arrlen = len(arr)

    if arrlen == 0:
        arr.insert(0, nr)
    else:
        i = 0
        while i < arrlen:
            if arr[i] > nr:
                break
            i += 1
        
        arr.insert(i, nr)

line = input.readline()

while line:
    twonrs = line.split()

    insertNumber(leftNrs, int(twonrs[0]))
    insertNumber(rightNrs, int(twonrs[1]))

    line = input.readline()

count = 0

totalDistance = 0

for i in range(len(leftNrs)):
    count += 1

    distance = abs(leftNrs[i] - rightNrs[i])

    totalDistance += distance

    #if count > 2:
    #    break

print(count)
print(totalDistance)