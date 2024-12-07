input = open('input_day1.txt', 'r')

leftNrs = []
rightNrs = []

def insertNumber(arr, nr):
    arrlen = len(arr)

    if arrlen == 0:
        arr.insert(0, [nr, 1])
    else:
        i = 0
        insert = True
        while i < arrlen:
            if arr[i][0] == nr:
                arr[i][1] += 1
                insert = False
                break
            elif arr[i][0] > nr:
                break

            i += 1
        
        if insert:
            arr.insert(i, [nr, 1])

line = input.readline()

while line:
    twonrs = line.split()

    insertNumber(leftNrs, int(twonrs[0]))
    insertNumber(rightNrs, int(twonrs[1]))

    line = input.readline()

totalSimilarity = 0

i = 0

j = 0

print(len(leftNrs))

while i < len(leftNrs):
    found = False

    lnr = leftNrs[i][0]

    print(f"lnr={lnr}")
    
    while j < len(rightNrs):
        rnr = rightNrs[j][0]

        #print(f"rnr={rnr}")

        if lnr < rnr:
            break

        if lnr == rnr:
            print(f"found {leftNrs[i][0]} times {rightNrs[j][1]}")
            found = True
            break

        j += 1
    
    if found:
        similarity = leftNrs[i][0] * rightNrs[j][1]

        print(similarity)

        totalSimilarity += similarity
    
    i += 1
    
print(f"Total similarity: {totalSimilarity}")