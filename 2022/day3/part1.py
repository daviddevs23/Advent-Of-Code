data = []
sum = 0

with open("input.txt") as f:
    data = f.readlines()

for line in data:
    compartment1 = line[:len(line) // 2]
    compartment2 = line[len(line) // 2::]

    commonItem = ''.join(set(compartment1).intersection(compartment2))
    if (commonItem.isupper()):
        sum = sum + ord(commonItem) - 65 + 27
    else:
        sum = sum + ord(commonItem) - 96

print(sum)
