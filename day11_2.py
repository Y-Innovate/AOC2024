import sys

input = open('input_day11.txt', 'r')

nrs = input.read()

stones = nrs.split()

zero={}
one={}
two={}
three={}
four={}
five={}
six={}
seven={}
eight={}
nine={}

def buildArray(stoneParm):
    global maxarraysize

    print(f"Build array {stoneParm}")

    stones = [stoneParm]

    for blink in range(0, maxarraysize):
        newStones = []
        for stone in stones:
            if stone == '0':
                newStones.append('1')
            elif len(stone) % 2 == 0:
                halflen = int(len(stone) / 2)
                leftStone = str(int(stone[0:halflen]))
                rightStone = str(int(stone[halflen:len(stone)]))

                newStones.append(leftStone)
                newStones.append(rightStone)
            else:
                newStones.append(str(int(stone) * 2024))
        stones = newStones

        sys.stdout.write(f"\r{blink}")

        match stoneParm:
            case '0':
                zero[blink] = stones
            case '1':
                one[blink] = stones
            case '2':
                two[blink] = stones
            case '3':
                three[blink] = stones
            case '4':
                four[blink] = stones
            case '5':
                five[blink] = stones
            case '6':
                six[blink] = stones
            case '7':
                seven[blink] = stones
            case '8':
                eight[blink] = stones
            case '9':
                nine[blink] = stones

    print("\n")

counter = 0

def recursiveBlink(level, stone):
    global maxlevel
    global maxarraysize
    global counter

    counter += 1

    if counter % 1000000 == 0:
        sys.stdout.write(f"\r{counter}")

    if level < maxlevel:
        if len(stone) % 2 == 0:
            halflen = int(len(stone) / 2)
            leftStone = str(int(stone[0:halflen]))
            rightStone = str(int(stone[halflen:len(stone)]))

            add = recursiveBlink(level + 1, leftStone)
            add += recursiveBlink(level + 1, rightStone)
        elif len(stone) == 1:
            add = 0
            match stone:
                case '0':
                    nrarray = zero
                case '1':
                    nrarray = one
                case '2':
                    nrarray = two
                case '3':
                    nrarray = three
                case '4':
                    nrarray = four
                case '5':
                    nrarray = five
                case '6':
                    nrarray = six
                case '7':
                    nrarray = seven
                case '8':
                    nrarray = eight
                case '9':
                    nrarray = nine

            if level < maxlevel - maxarraysize:
                entry = maxlevel - level
                while entry > maxarraysize:
                    entry -= maxarraysize
                for newstone in nrarray[entry - 1]:
                    add += recursiveBlink(level + entry, newstone)
            else:
                add = len(nrarray[maxlevel - level - 1])
        else:
            add = recursiveBlink(level + 1, str(int(stone) * 2024))

        return add
    else:
        return 1

maxarraysize = 40

buildArray('0')
buildArray('1')
buildArray('2')
buildArray('3')
buildArray('4')
buildArray('5')
buildArray('6')
buildArray('7')
buildArray('8')
buildArray('9')

maxlevel = 75

totalStones = 0

for stone in stones:
    print(f"\nStone {stone}")

    totalStones += recursiveBlink(0, stone)
#    
#    break

print(f"Total: {totalStones}")