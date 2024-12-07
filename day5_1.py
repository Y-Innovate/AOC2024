import re

input = open('input_day5.txt', 'r')

rules = {}

line = input.readline()

while line:
    if len(line) <= 1:
        break

    x = re.search("(\d+)\|(\d+)", line)

    nr1 = int(x.group(1))
    nr2 = int(x.group(2))

    if not nr1 in rules:
        rules[nr1] = []

    rules[nr1].append(nr2)

    line = input.readline()

print(rules)

total = 0

line = input.readline()

while line:
    nrs = line.split(",")

    correct = True

    for idx, nr in enumerate(nrs):
        nrs[idx] = int(nr)

    for idx, nr in enumerate(nrs):
        if idx > 0:
            if nr in rules:
                for i in range(0, idx):
                    if nrs[i] in rules[nr]:
                        correct = False
                        break
        
        if not correct:
            break
    
    if correct:
        middleidx = int((len(nrs) + 1) / 2) - 1
        middlenr = nrs[middleidx]

        total += middlenr

    line = input.readline()

print(f"Total: {total}")