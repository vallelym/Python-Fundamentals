import random
def roll_dice():
    return random.randint(1,6)

result = roll_dice()
print(f"You rolled a {result}!")