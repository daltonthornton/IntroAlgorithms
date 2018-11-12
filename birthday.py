import random

roomSize = 30
numTrials = 500
dupeCount = 0

for trial in range(numTrials):
    birthdayList = []
    for i in range(roomSize):
        newBDay = random.randrange(365)
        birthdayList.append(newBDay)

    foundDupe = False
    for num in birthdayList:
        if birthdayList.count(num) > 1:
            foundDupe = True

    if foundDupe == True:
        dupeCount = dupeCount + 1

prob = dupeCount / numTrials
print("Probabiltiy of shared birthdays in group size of ", roomSize, " is ", prob)
