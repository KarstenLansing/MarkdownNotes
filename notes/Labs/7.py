import re

def getInput():
    d = {"/": {}}
    for x in open("Labs/input.txt"):
        if x[0].isdigit():
            d["/"][str(x)[x.find(" "):-1]] = int(re.findall(r'\d+', x)[0])
        elif x[0] != "$":
            d[x[0:3]] = x[4:].strip("\n")
    return d 

           

        
    
def part1():
    X = getInput()
    print(X)

if __name__ == "__main__":
    part1()
