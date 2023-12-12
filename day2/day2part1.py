with open('day2.in') as file:
    rounds = [i.replace(" ", "") for i in file.read().strip().split("\n")]

outcomes = {
    "AX": 4, "AY": 8, "AZ": 3,
    "BX": 1, "BY": 5, "BZ": 9,
    "CX": 7, "CY": 2, "CZ": 6
}

total_score_p1 = 0
for round in rounds:
    total_score_p1 += outcomes[round]

print("la réponse est :", total_score_p1)
