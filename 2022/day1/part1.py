data = []

with open("input.txt") as f:
    data = f.readlines();

max = 0
current = 0

for line in data:
    line = line.replace("\n", "")
    if line == "":
        if current > max:
            max = current
        current = 0

    else:
        current = current + int(line)

print(max)
