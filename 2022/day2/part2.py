data = []
score = 0

points = {"A":1, "B":2, "C":3}
gameResults = {"X":0, "Y":3, "Z":6}

with open("input.txt") as f:
    data = f.readlines()

for row in data:
    row.replace("\n", "")
    row = row.split()
    score = score + gameResults[row[1]]

    # A = Rock
    # B = Paper
    # C = Scissors
    if (row[0] == "A"):
        # Lose
        if (row[1] == "X"):
            score = score + points["C"]
        # Draw
        elif (row[1] == "Y"):
            score = score + points["A"]
        # Win
        elif (row[1] == "Z"):
            score = score + points["B"]
    elif (row[0] == "B"):
        # Lose
        if (row[1] == "X"):
            score = score + points["A"]
        # Draw
        elif (row[1] == "Y"):
            score = score + points["B"]
        # Win
        elif (row[1] == "Z"):
            score = score + points["C"]
    elif (row[0] == "C"):
        # Lose
        if (row[1] == "X"):
            score = score + points["B"]
        # Draw
        elif (row[1] == "Y"):
            score = score + points["C"]
        # Win
        elif (row[1] == "Z"):
            score = score + points["A"]

print(score)
