import re

input = open('input_day3.txt', 'r')

text = input.read()

x = re.findall("mul\(([0-9]+),([0-9]+)\)|(do\(\))|(don't\(\))", text)

total = 0
itCounts = True

for mtch in x:
    if mtch[3] == "don't()":
        itCounts = False
    elif mtch[2] == "do()":
        itCounts = True
    elif itCounts:
        nr1 = int(mtch[0])
        nr2 = int(mtch[1])

        total += nr1 * nr2

print(f"Total: {total}")