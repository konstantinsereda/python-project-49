#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/konst/Hexlet/python-project-49/brain_games')
from cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    print('Hello, ' + welcome_user() + '!')


if __name__ == '__main__':
    main()
