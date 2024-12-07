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

def correctUpdate(somenrs):
    correct = True

    for idx, nr in enumerate(nrs):
        if idx > 0:
            if nr in rules:
                for i in range(0, idx):
                    if nrs[i] in rules[nr]:
                        savenr = nrs[i]
                        nrs[i] = nr
                        nrs[idx] = savenr

                        correct = False
                        break
        
        if not correct:
            break
    
    return correct

total = 0

line = input.readline()

while line:
    nrs = line.split(",")

    for idx, nr in enumerate(nrs):
        nrs[idx] = int(nr)

    if not correctUpdate(nrs):
        while not correctUpdate(nrs):
            continue

        middleidx = int((len(nrs) + 1) / 2) - 1
        middlenr = nrs[middleidx]

        total += middlenr

    line = input.readline()

print(f"Total: {total}")