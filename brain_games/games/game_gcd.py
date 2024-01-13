import random
import prompt
import math
GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_game():
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    question = f"Question: {random_number1} {random_number2}"
    result = math.gcd(random_number1, random_number2)
    return question, result


def is_answer(right_answer, answer):
    answer = int(answer)
    return right_answer == answer
