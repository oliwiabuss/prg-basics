import random
dice = random.randint(1, 6)
special_dice = dice == 1 or dice == 6
print(f'your number is {dice} and you have special number is {special_dice}')