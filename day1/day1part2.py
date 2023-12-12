with open('day1.in', 'r') as file:
    lines = file.read().strip().split("\n")

    elf_calories = []
    current_elf_calories = 0

for line in lines:
    if line:
        current_elf_calories += int(line)
    else:
        elf_calories.append(current_elf_calories)
        current_elf_calories = 0

elf_calories.append(current_elf_calories)

sorted_elf_calories = sorted(elf_calories, reverse=True)

total_top_three_calories = sum(sorted_elf_calories[:3])

print("la répons est :", total_top_three_calories)
