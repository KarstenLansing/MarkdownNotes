def getInput():
    for l in open('Labs/input.txt'):
        yield [i.split("-") for i in l.strip("\n").split(",")]
    

def part1():
    X = getInput()
    counter = 0
    for i in X:
        i = [[int(j) for j in k] for k in i]
        if (i[0][0] >= i[1][0] and i[0][1] <= i[1][1]) or (i[0][0] <= i[1][0] and i[0][1] >= i[1][1]):
            counter += 1
    return counter

def part2():
    X = getInput()
    counter = 0
    for i in X:
        i = [[int(j) for j in k] for k in i]
        if (i[0][0] <= i[1][0] <= i[0][1]) or (i[1][0] <= i[0][0] <= i[1][1]):
            counter += 1
    return counter

if __name__ == '__main__':
    print(part1())
    print(part2())