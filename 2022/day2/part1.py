data = []
score = 0

points = {"X":1, "Y":2, "Z":3}
moves = {"A":"X", "B":"Y", "C":"Z"}

with open("input.txt") as f:
    data = f.readlines()

for row in data:
    row.replace("\n", "")
    row = row.split()
    row[0] = moves[row[0]]
    if (row[0] == row[1]):
        score = score + 3 + points[row[1]]
    else:
        score = score + points[row[1]]
        if (row[0] == "X"):
            if (row[1] == "Y"):
                score = score + 6
        elif (row[0] == "Y"):
            if (row[1] == "Z"):
                score = score + 6
        elif (row[0] == "Z"):
            if (row[1] == "X"):
                score = score + 6

print(score)
