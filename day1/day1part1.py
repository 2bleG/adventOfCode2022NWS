with open("day1.in", "r") as file:
    data = file.read()

lines = data.strip().split("\n")

current_elf_calories = 0
max_elf_calories = 0

for line in lines:
    if line:
        current_elf_calories += int(line)
    else:
        if current_elf_calories > max_elf_calories:
            max_elf_calories = current_elf_calories
        current_elf_calories = 0

if current_elf_calories > max_elf_calories:
    max_elf_calories = current_elf_calories

print("la répons est :", max_elf_calories)
