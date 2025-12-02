import os

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    data = f.read()
    ip = [r for r in data.split(',')]
    ip = [r.split('-') for r in ip]

# Part 1
sum  = 0
for i in ip:
    for j in range(int(i[0]), int(int(i[1])+1)):
        j = str(j)
        if j[0] == 0:                       # Check for first digit not equal zero
            sum += int(j)
            continue

        jlen = len(j)
        if jlen % 2 == 0:
            if j[:jlen//2] == j[-((jlen//2)):]:
                sum += int(j)
    
print("Result1:", sum)

# Part 2
sum  = 0
for i in ip:
    for j in range(int(i[0]), int(int(i[1])+1)):
        j = str(j)
        if j[0] == 0:                       # Check for first digit not equal zero
            sum += int(j)
            continue

        jlen = len(j)
        for k in range(1, jlen//2+1):
            if jlen % k == 0:
                if j == j[:k] * (jlen // k):
                    sum += int(j)
                    break
    
print("Result2:", sum)