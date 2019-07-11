import random

print('What is your name?')
name = input()
print('Hello, ' +name+ '!')

diceA = random.randint(1,6)
diceB = random.randint(1,6)
diceC = random.randint(1,6)
print('Rolling the dice...')
print('Die 1: '+str(diceA))
print('Die 2: '+str(diceB))
print('Die 2: '+str(diceC))

total = diceA + diceB + diceC
print('Total value: '+str(total))

if total > 10:
    print(+name+ ' won')
else: print(+name+ ' lost')
