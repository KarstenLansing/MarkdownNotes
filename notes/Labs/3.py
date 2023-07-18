import string 


myList = [i.split('\t')[0] for i in string.ascii_lowercase+string.ascii_uppercase]

def valueOfLetter(letter):
    for i in range(len(myList)):
        if letter in myList[i]:
            return i+1

def getHashmapOfWord(word):
    hashmap = {}
    for i in range(len(word)):
        hashmap[word[i]] = 1
    return hashmap


def part2():
    X = [str(l.split()).strip("\'\"[]") for l in open('Labs/input.txt')]
    X = [X[i:i+3] for i in range(0, len(X), 3)]
    totalpoints = 0
    
    for i in range(len(X)):
        #check all 3 elements in X for a common letter
        hashmap1 = getHashmapOfWord(X[i][0])
        hashmap2 = getHashmapOfWord(X[i][1])
        hashmap3 = getHashmapOfWord(X[i][2])
        for j in range(len(X[i][0])):
            if X[i][0][j] in hashmap2 and X[i][0][j] in hashmap3:
                totalpoints += valueOfLetter(X[i][0][j])
                break
            elif X[i][1][j] in hashmap1 and X[i][1][j] in hashmap3:
                totalpoints += valueOfLetter(X[i][1][j])
                break
            elif X[i][2][j] in hashmap1 and X[i][2][j] in hashmap2:
                totalpoints += valueOfLetter(X[i][2][j])
                break

    return (totalpoints)

