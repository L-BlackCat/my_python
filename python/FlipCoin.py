import random
for experimentNumber in range(10000):
# Code that creates a list of 100 'heads' or 'tails' values.
    numberOfStreaks = 0
    list = []
    for i in range(100):
        randNum = random.randint(0,1)
        list.append(randNum)

    i = 0
    while i < 94:
        tempList = list[i:i+6]
        i+= 1
        if (0 in tempList) and (1 in tempList):
            continue
        numberOfStreaks += 1
    # Code  that checks if there is a streak of 6 heads or tails in a row.
    print('Chance of streak: %s%%' % (numberOfStreaks / 100))

