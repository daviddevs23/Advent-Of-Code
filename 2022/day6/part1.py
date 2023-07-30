data = ""

with open("input.txt") as f:
    data = f.readlines()[0].strip("\n")

size = len(data)

for i in range(0, size):
    if len(set(data[i:i+14])) == 14:
        print(i + 14)
        break
