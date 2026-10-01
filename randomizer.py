"""#testing tähendab uus kood mida saab kustudada veel"""

import random
import math #sum()tundub parem kui mingi muu viis kokku liita

chance = int(float(input("Input here for chance: ")))


def randomizer():
    rolls = 1
    while random.randint(1, chance) != 1:
        rolls +=1
    print(rolls) #tahaks panna mingi print(f" #(number){rolls}") et on prindi number ees nn
    #return rolls #testing

how_many_times = int(float(input("Input here for amount of times: ")))

while how_many_times != 0:
    how_many_times -= 1 # -= oli =, ei tea miks peab -= olema, pidin otsima netist
    randomizer()
    #total = sum(idk_what_to_call_this) #testing
    #print(total) #testing

#idk_what_to_call_this = randomizer() # testing




# kõik rollid kokku liita