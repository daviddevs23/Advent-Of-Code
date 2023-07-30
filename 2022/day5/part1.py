stacks = []
data = []

numIndex = 0
numStacks = 0

with open("./input.txt") as f:
    data = f.readlines()

# Find number of stacks
while "[" in data[numIndex]:
    numIndex += 1

numStacks = int(data[numIndex].replace(" \n", "").split(" ")[-1])

# Fill stacks with data
for i in range(numStacks):
    stacks.append([])

for i in range(numStacks,-1,-1):
    for k in range(0, numStacks * 4, 4):
        tmp = data[i][k:k+4]
        if "[" in tmp:
             stacks[k // 4].append(tmp.replace("[", "").replace("]", "").replace("\n", ""))

# Follow through with instructions
for line in data:
    if ("move") in line:
        tmp = line.split(" ")
        numMoves = int(tmp[1])
        start = int(tmp[3]) - 1
        end = int(tmp[5]) - 1

        for i in range(numMoves):
            tmp = stacks[start].pop(i - numMoves)
            stacks[end].append(tmp)

res = ""
for i in stacks:
    if len(i) > 0:
        res = res + i.pop().replace(" ", "")

print(res)
