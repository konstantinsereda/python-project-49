# Опишите эту логику в функции welcome_user файла brain_games/cli.py
# поместите вызов этой функции в скрипт brain_games/scripts/brain_games.py

import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    return name
