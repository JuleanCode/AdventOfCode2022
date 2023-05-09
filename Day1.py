elfCalories = []

with open('Input/Day1.txt') as f:
    lines = f.readlines()
    
    Calories = 0
    for line in lines:
        if line == "\n":
            elfCalories.append(int(Calories))
            Calories = 0
        else:
            Calories += int(line)
    print('The elf with the most calories has:')
    print(max(elfCalories))