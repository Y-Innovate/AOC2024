import struct

class Entry:
    prevEntry = None
    nextEntry = None
    entryType = ''

class File(Entry):
    def __init__(self, id, count, offset):
        self.id = id
        self.count = count
        self.offset = offset
        self.entryType = 'F'
        self.wasMoved = False

class Freespace(Entry):
    def __init__(self, count, offset):
        self.count = count
        self.offset = offset
        self.entryType = '.'

input = open('input_day9.txt', 'r')

id = 0

doFreeSpace = False

firstEntry = None
prevEntry = None
lastEntry = None
offset = 0

id3 = None

char = input.read(1)

while char:
    count = int(char)

    if not doFreeSpace:
        lastEntry = File(id, count, offset)
        if firstEntry == None:
            firstEntry = lastEntry
            prevEntry = lastEntry
        else:
            prevEntry.nextEntry = lastEntry
            lastEntry.prevEntry = prevEntry
            prevEntry = lastEntry

        if lastEntry.id == 3:
            id3 = lastEntry

        doFreeSpace = True
        id += 1
    else:
        if count != 0:
            entry = Freespace(count, offset)
            if firstEntry == None:
                firstEntry = entry
            else:
                prevEntry.nextEntry = entry
                entry.prevEntry = prevEntry
                prevEntry = entry

        doFreeSpace = False

    offset += count

    char = input.read(1)

firstFreespace = firstEntry

while lastEntry != None:
    newLastEntry = lastEntry.prevEntry

    if lastEntry.entryType == 'F' and lastEntry.wasMoved == False:
        print(f"Processing {lastEntry.id} with length {lastEntry.count} at offset {lastEntry.offset}")

        #if lastEntry.id == 5400:
        #    break

        someEntry = firstFreespace
        firstFreespaceMoved = False

        while someEntry != None:
            if firstFreespaceMoved == False and someEntry.entryType == '.' and someEntry.count > 0:
                firstFreespace = someEntry
                firstFreespaceMoved = True
            
            if someEntry.entryType == 'F' and someEntry.wasMoved == False and someEntry.offset > lastEntry.offset:
                break
            elif someEntry.entryType == '.' and someEntry.offset > lastEntry.offset:
                break

            if someEntry.entryType == '.' and someEntry.count >= lastEntry.count:
                print(f"Gets moved to offset {someEntry.offset}")

                newFreeSpace = Freespace(lastEntry.count, lastEntry.offset)

                newFreeSpace.nextEntry = lastEntry.nextEntry
                if lastEntry.nextEntry != None:
                    lastEntry.nextEntry.prevEntry = newFreeSpace
                newFreeSpace.prevEntry = lastEntry.prevEntry
                if lastEntry.prevEntry != None:
                    lastEntry.prevEntry.nextEntry = newFreeSpace

                someEntry.count -= lastEntry.count
                if someEntry.prevEntry != None:
                    someEntry.prevEntry.nextEntry = lastEntry
                lastEntry.prevEntry = someEntry.prevEntry
                lastEntry.offset = someEntry.offset
                if someEntry.count > 0:
                    lastEntry.nextEntry = someEntry
                    someEntry.prevEntry = lastEntry
                    someEntry.offset += lastEntry.count
                else:
                    lastEntry.nextEntry = someEntry.nextEntry
                    if someEntry.nextEntry != None:
                        someEntry.nextEntry.prevEntry = lastEntry

                lastEntry.wasMoved = True

                break
            
            someEntry = someEntry.nextEntry

    lastEntry = newLastEntry

output = open('output_day9_2.txt', 'wb')

someEntry = firstEntry

while someEntry != None:
    if someEntry.entryType == 'F':
        s = struct.pack('<i', someEntry.id)

        for i in range(0, someEntry.count):
            output.write(s)
    
    elif someEntry.entryType == '.' and someEntry.count > 0:
        s = struct.pack('<i', -1)

        for i in range(0, someEntry.count):
            output.write(s)

    someEntry = someEntry.nextEntry

output.close()

input2 = open('output_day9_2.txt', 'rb')

pos = 0

checksum = 0

someDWord = input2.read(4)

while someDWord:
    someInt = struct.unpack('<i', someDWord)

    if someInt[0] > 0:
        checksum += someInt[0] * pos

    pos += 1

    someDWord = input2.read(4)

print(f"Checksum: {checksum}")