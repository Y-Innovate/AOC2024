import re

input = open('input_day7.txt', 'r')

def calculateIt(operands, operators, opcount, cat, targetOutcome):
    outcome = operands[0]

    for op in range(0, opcount - 1):
        if cat & 2**op:
            outcome = int(str(outcome) + str(operands[op+1]))
        else:
            if operators & 2**op:
                outcome = outcome + operands[op+1]
            else:
                outcome = outcome * operands[op+1]
        
        if outcome > targetOutcome:
            outcome = 0
            break
    
    return outcome

def canItBeTrue(outcome, operands):
    itCan = False

    for cat in range(0, 2**len(operands)-1):
        for op in range(0, 2**(len(operands)-1)):
            if not cat & op:
                thisOutcome = calculateIt(operands, op, len(operands), cat, outcome)

                if thisOutcome == outcome:
                    itCan = True
                    break
        
        if itCan:
            break
    
    return itCan

total = 0

linecount = 0

line = input.readline()

while line:
    linecount += 1

    print(f"Line {linecount}")

    x = re.findall("(\d+)", line)

    outcome = int(x[0])
    operands = {}

    for i in range(0, len(x) - 1):
        operands[i] = int(x[i+1])
    
    if canItBeTrue(outcome, operands):
        total += outcome

    line = input.readline()

print(f"Total: {total}")