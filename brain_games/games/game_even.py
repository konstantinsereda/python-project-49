import random
import prompt
GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
GAME_ROUNDS = 3


def get_game():
    question = random.randint(1, 100)
    if question % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return question, result


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def is_answer(right_answer, answer):
    return right_answer == answer
