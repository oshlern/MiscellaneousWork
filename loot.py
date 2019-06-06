# There are 3 levels of chests
# Each chest has a 2/5 chance for a ring, 2/5 for a potion, and 1/5 for a weapon
# Each one of those has its own separate table with percentages and such, depending on the level of chest
# And each chest also procures a random number of gold
# Last but not least, each chest has a way of determining how much extra loot there is in the chest
# Which involves a probability that decreases after each successful roll

import random



bronze_ps = {"gold sword": 0.1, "armor": 0.2}
silver_ps = {"gold sword": 0.1, "armor": 0.2}
gold_ps = {"gold sword": 0.1, "armor": 0.2}
chest_ps = {1: bronze_ps, 2: silver_ps, 3: gold_ps}

bronze_g = (10,20)
silver_g = (10,20)
gold_g = (10,20)
chest_gold = {1: bronze_g, 2: silver_g, 3: gold_g}

def open(level):
    Max, Min = chest_gold[level]
    gold = Min + (Max - Min) *  random.random()
    loot = pick_item(chest_ps[level])
    


def pick_item(ps): # takes in dictionary
    total = sum(ps.values())
    rand = total*random.random()
    for item in ps:
        if rand < ps[item]:
            return item
        else:
            rand -= ps[item]


