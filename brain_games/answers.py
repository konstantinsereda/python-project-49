import prompt

answer = ''


def hello():
    user_name = prompt.string("Welcome to the Brain Games! \nMay \
                              I have your name? ")
    return user_name


def rule_even():
    print('Answer "yes" if the number is even, \
    otherwise answer "no".')


def user_answer():
    global answer
    answer = prompt.string('Your answer: ')
    return answer
