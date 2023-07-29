data = []
sum = 0

with open("input.txt") as f:
    data = f.readlines()

sizeOfData = len(data)

for i in range(0, sizeOfData, 3):
    compartment1 = data[i]
    compartment2 = data[i+1]
    compartment3 = data[i+2]

    commonItem = ''.join(set(compartment1).intersection(compartment2).intersection(compartment3)).replace("\n", "")
    if (commonItem.isupper()):
        sum = sum + ord(commonItem) - 65 + 27
    else:
        sum = sum + ord(commonItem) - 96

print(sum)
