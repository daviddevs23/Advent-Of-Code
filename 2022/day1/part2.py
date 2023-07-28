data = []

with open("input.txt") as f:
    data = f.readlines();

maxes = [0,0,0]
current = 0

for line in data:
    line = line.replace("\n", "")
    if line == "":
        if current > maxes[0]:
            maxes[0] = current
            maxes.sort()
        current = 0

    else:
        current = current + int(line)

print(sum(maxes))
