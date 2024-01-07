import random
import math


def even_question():
    number = random.randint(1, 100)
    print(f"Question: {number}")
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def calc_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    math_oper = random.randint(1, 3)
    if math_oper == 1:
        result = a * b
        print(f"Question: {a} * {b} ")
        return result

    elif math_oper == 2:
        result = a + b
        print(f"Question: {a} + {b} ")
        return result

    elif math_oper == 3:
        result = a - b
        print(f"Question: {a} - {b} ")
        return result


def gcd_question():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print(f"Question: {a} {b}")
    return math.gcd(a, b)
