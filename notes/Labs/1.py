

X = [l.strip() for l in open('Labs/input.txt').readlines()]

Q = []
for elf in ('\n'.join(X)).split('\n\n'):
    q = 0
    for x in elf.split('\n'):
        q += int(x)
    Q.append(q)
Q.sort()
print(Q[-1] + Q[-2] + Q[-3])