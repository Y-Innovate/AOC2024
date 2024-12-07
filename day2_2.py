input = open('input_day2.txt', 'r')

def testSafe(nrs, direction):
    safe = True

    lastnr = 0

    for idx, nr in enumerate(nrs):
        if idx > 0:
            diff = (nr - lastnr) * direction

            if diff < 1 or diff > 3:
                safe = False
                break
        
        lastnr = nr
    
    return safe


totalSafe = 0

line = input.readline()

while line:
    nrs = line.split()

    for idx, nr in enumerate(nrs):
        nrs[idx] = int(nr)

    direction = 1

    if nrs[0] > nrs[len(nrs) - 1]:
        direction = -1

    safe = testSafe(nrs, direction)

    if not safe:
        for idx in range(0, len(nrs)):
            nrs2 = nrs.copy()
            del nrs2[idx]

            safe = testSafe(nrs2, direction)

            if safe:
                break

    if safe:
        totalSafe += 1

    line = input.readline()

print(f"Total safe: {totalSafe}")