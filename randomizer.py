"""#testing tähendab uus kood mida saab kustudada veel"""

import random

chance = int(float(input("Input here for chance: ")))


def randomizer():
    rolls = 1
    while random.randint(1, chance) != 1:
        rolls +=1
    print(rolls)
    #rolls_total = 0 + rolls
    #print(rolls_total)


how_many_times = int(float(input("Input here for amount of times: ")))

while how_many_times != 0:
    how_many_times -= 1
    randomizer()
    
