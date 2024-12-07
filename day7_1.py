import re

input = open('input_day7.txt', 'r')

def calculateIt(operands, operators, opcount):
    outcome = operands[0]

    for op in range(0, opcount - 1):
        if operators & 2**op:
            outcome = outcome + operands[op+1]
        else:
            outcome = outcome * operands[op+1]
    
    return outcome

def canItBeTrue(outcome, operands):
    itCan = False

    for op in range(0, 2**(len(operands)-1)):
        thisOutcome = calculateIt(operands, op, len(operands))

        if thisOutcome == outcome:
            itCan = True
            break
    
    return itCan

total = 0

line = input.readline()

while line:
    x = re.findall("(\d+)", line)

    outcome = int(x[0])
    operands = {}

    for i in range(0, len(x) - 1):
        operands[i] = int(x[i+1])
    
    if canItBeTrue(outcome, operands):
        total += outcome

    line = input.readline()

print(f"Total: {total}")