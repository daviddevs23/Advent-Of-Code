data = []
sum = 0

with open("input.txt") as f:
    data = f.readlines()

for line in data:
    line = line.replace("\n","").split(",")
    line[0] = line[0].split("-")
    line[1] = line[1].split("-")

    line[0][0] = int(line[0][0])
    line[0][1] = int(line[0][1])
    line[1][0] = int(line[1][0])
    line[1][1] = int(line[1][1])

    if (line[0][0] <= line[1][1] and line[0][1] >= line[1][1]):
        sum = sum + 1
    elif (line[0][0] <= line[1][0] and line[0][1] >= line[1][0]):
        sum = sum + 1

print(sum)
