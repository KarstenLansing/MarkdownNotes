import string
import re

def processInput():
    instructions = []
    columns = []
    b = False

    for i in open('Labs/input.txt'):
        if len(i) < 2: continue
        if i[1].isdigit():
            b = True
            continue
        elif b:
            instructions.append([int(k) for k in re.findall(r'\d+', i)])
        else:
            i = ([str(i[l:l+3]).strip("[]\n ") for l in range(0, len(i), 4)])
            for j in range(len(i)):
                if len(columns) <= j: columns.append([i[j]])
                else: columns[j].append(i[j])
        
    return [columns, instructions]


def getDepth(state):
    counter = 0
    for i in state:
        if i == '':
            counter += 1
        else: break

    return counter


def MoveState(state : list[list], instructions: list):

    for i in range(instructions[0]):
        temp = state[instructions[1]-1].pop(getDepth(state[instructions[1]-1]))
        state[instructions[2]-1].insert(getDepth(state[instructions[2]-1]), temp)
    return state

def MoveState2(state : list[list], instructions: list):

    for i in range(instructions[0]):
        temp = state[instructions[1]-1][getDepth(state[instructions[1]-1])]
        state[instructions[2]-1].insert(getDepth(state[instructions[2]-1]), temp)
        
    
    return state

def part2():
    D = processInput()
    for i in D[1]:
        print(D[0])
        D[0] = MoveState2(D[0], i)
    for i in D[0]:
        print(i[getDepth(i)], end=' ')


def part1():
    D = processInput()
    for i in D[1]:
        print(D[0])
        D[0] = MoveState(D[0], i)
    #print the D[0] index of getDepth for each column
    for i in D[0]:
        print(i[getDepth(i)], end='')
        
    

if __name__ == '__main__':
    part1()