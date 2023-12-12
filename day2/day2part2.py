with open('day2.in') as file:
    rounds = [i.replace(" ", "") for i in file.read().strip().split("\n")]

desired_outcomes = {
    "AX": 3, "AY": 4, "AZ": 8,
    "BX": 1, "BY": 5, "BZ": 9,
    "CX": 2, "CY": 6, "CZ": 7
}

total_score_p2 = 0
for round in rounds:
    total_score_p2 += desired_outcomes[round]

print("la répons est :", total_score_p2)
