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


def progression_question():
    start = random.randint(1, 30)
    k = random.randint(6, 10)
    diff = random.randint(1, 5)
    cut_position = random.randint(0, k - 1)
    result = []
    for i in range(k):
        result.append(start + i * diff)
    hidden_number = result[cut_position]
    result[cut_position] = '..'
    print('Question:', ' '.join([str(x) for x in result]))
    return hidden_number


def prime_question():
    n = random.randint(2, 100)
    print(f"Question: {n}")
    # this flag maintains status whether the n is prime or not
    prime_flag = 0
    if (n > 1):
        for i in range(2, int(math.sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return 'yes'
        else:
            return 'no'
