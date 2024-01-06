import random


def even_question():
    number = random.randint(1, 100)
    print(f"Question: {number}")
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'
