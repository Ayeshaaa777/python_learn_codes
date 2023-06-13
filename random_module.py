import random

x = random.randint(1, 6)
print(x)  # random integer between 1 and 6

y = random.random()
print(y)  # random integer between 0 and 1

mylist = ['rock', 'paper', 'scissor']
z = random.choice(mylist)
print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "Q", "K", "J", "A"]
random.shuffle(cards)

print(cards)
