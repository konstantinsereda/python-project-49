import prompt


def hello():
    user_name = prompt.string("Welcome to the Brain Games!\
     \nMay I have your name? ")
    return user_name


def rule_even():
    print('Answer "yes" if the number is even, \
    otherwise answer "no".')


def rule_calc():
    print('What is the result of the expression?')


def user_answer():
    answer = prompt.string('Your answer: ')
    return answer
