input = open('input_day11.txt', 'r')

nrs = input.read()

nrs = "17"

stones = nrs.split()

for blink in range(0, 12):
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

print(f"Total: {len(stones)}")