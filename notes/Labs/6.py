
def input():
    j = ""
    for i in open("Labs/input.txt"):
        j += str(i).strip("\n")
    return j

def uniquechar(s):
    if len(s) == len(set(s)):
        return True
    else:
        return False

def part1():
    state = input()
    marker = ""
    for i in range(len(state)):
        if uniquechar(marker) and len(marker) == 4:
            print(i+3, marker)
            break
        marker = state[i:i+4]

def part2():
    state = input()
    marker = ""
    for i in range(len(state)):
        if uniquechar(marker) and len(marker) == 14:
            print(i+ 13, marker)
            break
        marker = state[i:i+14]
        

if __name__ == "__main__":
    part2()

    