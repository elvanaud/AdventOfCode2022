#TODO: faire ça en rust pour apprendre

lines = open("input.txt").read().split("\n")

maxCalories = 0
calories = 0
for line in lines:
    if line == "":
        if calories >= maxCalories: maxCalories = calories 
        calories = 0
        continue
    calories += int(line)

print(maxCalories)

########
#exo2
def sumElf(lines):
    sum = 0
    for line in lines:
        if line == "":
            yield sum
            sum = 0
        else:
            sum += int(line)
            
elfCalories = list(sumElf(lines))
elfCalories.sort(reverse = True)
print(sum(elfCalories[0:3]))