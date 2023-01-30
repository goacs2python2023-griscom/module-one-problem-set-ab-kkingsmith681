"""Write a function that uses the random package and rolls two dice. The function should return "win" if the sum of those two dice is 6, 7 or 8 and returns "lose" otherwise"""

def rollDice():
    import random
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(str(dice1) + " and " + str(dice2))

    if dice1 + dice2 == 6 or dice1 + dice2 == 7 or dice1 + dice2 == 8:
        return "win"
    else:
        return "lose"

print(rollDice())
