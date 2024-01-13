import random
import prompt

GAME_RULE = "What is the result of the expression?"


def calculate_result(random_number_1, random_number_2, math_operator):
    if math_operator == "*":
        result = random_number_1 * random_number_2

    elif math_operator == "+":
        result = random_number_1 + random_number_2

    else:
        result = random_number_1 - random_number_2
    return str(result)


def get_game():
    random_number_1 = random.randint(1, 10)
    random_number_2 = random.randint(1, 10)
    math_operator = random.choice(["*", "-", "+"])
    question = f"Question: {random_number_1} {math_operator} {random_number_2}"
    result = calculate_result(random_number_1, random_number_2, math_operator)
    return question, result


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def is_answer(right_answer, answer):
    answer = answer
    return right_answer == answer
