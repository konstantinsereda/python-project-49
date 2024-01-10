import random
import prompt

GAME_RULE = "What number is missing in the progression?"
GAME_ROUNDS = 3


def get_game():
    start = random.randint(1, 30)
    k = random.randint(6, 10)
    diff = random.randint(1, 5)
    cut_position = random.randint(0, k - 1)
    result = []
    for i in range(k):
        result.append(start + i * diff)
    hidden_number = result[cut_position]
    result[cut_position] = '..'
    question = ('Question:', ' '.join([str(x) for x in result]))
    return question, hidden_number


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def is_answer(right_answer, answer):
    answer = int(answer)
    return right_answer == answer
