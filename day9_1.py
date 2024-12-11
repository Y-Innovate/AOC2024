import struct

input = open('input_day9.txt', 'r')

output = open('output_day9_1_1.txt', 'wb')

id = 0

doFreeSpace = False

reverseCounts = ""

char = input.read(1)

while char:
    count = int(char)

    for i in range(0, count):
        if not doFreeSpace:
            s = struct.pack('<i', id)
            output.write(s)
        else:
            s = struct.pack('<i', -1)
            output.write(s)

    if not doFreeSpace:
        reverseCounts = char + reverseCounts
        doFreeSpace = True
        id += 1
    else:
        doFreeSpace = False

    char = input.read(1)

output.close()

input2 = open('output_day9_1_1.txt', 'rb')

output2 = open('output_day9_1_2.txt', 'wb')

id -= 1
lastId = -1
pos = 0
count = int(reverseCounts[pos])

someDWord = input2.read(4)

while (someDWord):
    someInt = struct.unpack('<i', someDWord)

    if someInt[0] >= id:
        break

    if someInt[0] != -1:
        output2.write(someDWord)
        lastId = someInt[0]
    else:
        if count <= 0:
            pos += 1
            count = int(reverseCounts[pos])
            id -= 1

        if lastId >= id:
            break

        s = struct.pack('<i', id)
        output2.write(s)

        count -= 1

    someDWord = input2.read(4)

output2.close()

input3 = open('output_day9_1_2.txt', 'rb')

pos = 0

checksum = 0

someDWord = input3.read(4)

while someDWord:
    someInt = struct.unpack('<i', someDWord)

    checksum += someInt[0] * pos

    pos += 1

    someDWord = input3.read(4)

print(f"Checksum: {checksum}")