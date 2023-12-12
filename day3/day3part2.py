from string import ascii_letters

with open('day3.in') as file:
    data = [i for i in file.read().strip().split("\n")]

totalSum = 0
j = 3
for i in range(0, len(data), 3):
    entry = data[i:j]
    j += 3

    for value, character in enumerate(ascii_letters):
        if character in entry[0] and character in entry[1] and character in entry[2]:
            totalSum += value + 1


print("la réponse est: ", totalSum)