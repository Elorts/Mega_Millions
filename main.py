import random

your_numbers = []
winning_numbers = []
numbers_set = []
n = 5


def lottery_numbers_generator():
    numbers_set.clear()

    for number in range(n):
        numbers_set.append(random.randint(1, 70))

    numbers_set.append(random.randint(1, 25))
    return numbers_set


def is_equal(yn, wn):

    if yn[0] == wn[0] and yn[1] == wn[1] and yn[2] == wn[2] and yn[3] == wn[3] and yn[4] == wn[4] and yn[5] == wn[5]:

        return True
    else:
        return False


winner = False
purchases = 0

while not winner:
    your_numbers.clear()
    winning_numbers.clear()

    your_numbers = lottery_numbers_generator().copy()
    winning_numbers = lottery_numbers_generator().copy()

    purchases += 1
    print(purchases)

    if is_equal(your_numbers, winning_numbers):
        winner = True
        print(f"You have to buy {purchases} tickets to win Mega Millions at this time!")
