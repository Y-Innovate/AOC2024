import re

input = open('input_day3.txt', 'r')

text = input.read()

x = re.findall("mul\(([0-9]+),([0-9]+)\)", text)

total = 0

for mul in x:
    nr1 = int(mul[0])
    nr2 = int(mul[1])

    total += nr1 * nr2

print(f"Total: {total}")