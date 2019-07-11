import random

diceA = random.randint(1,6)
diceB = random.randint(1,6)
print('Rolling the dice...')
print('Die 1: '+str(diceA))
print('Die 2: '+str(diceB))

total = diceA + diceB
print('Total value: '+str(total))

if total > 7:
    print('You won')
else: print('You lost')
