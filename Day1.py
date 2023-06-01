#---Part 1---

elfCalories = []

with open('2022/Input/Day1.txt') as f:
    lines = f.readlines()
    
    calories = 0
    for line in lines:
        if line == "\n":
            elfCalories.append(int(calories))
            calories = 0
        else:
            calories += int(line)
    print('The elf with the most calories has:')
    print(max(elfCalories))

#---Part 2---

elfCalories.sort()
highestCalories = 0

for i in elfCalories[-3:]:
    highestCalories += i

print(highestCalories)
