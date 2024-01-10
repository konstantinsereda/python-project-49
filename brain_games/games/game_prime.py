import random
import prompt
import math

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
GAME_ROUNDS = 3


def get_game():
    random_number = random.randint(2, 100)
    prime_flag = 0
    if random_number > 1:
        for i in range(2, int(math.sqrt(random_number)) + 1):
            if random_number % i == 0:
                prime_flag = 1
                break
        if not prime_flag:
            result = 'yes'
        else:
            result = 'no'

    return random_number, result


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def is_answer(right_answer, answer):
    return right_answer == answer
