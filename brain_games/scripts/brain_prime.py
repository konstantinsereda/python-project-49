from brain_games.answers import hello, rule_prime, user_answer
from brain_games.questions import prime_question


def main():
    attempt = 0
    user_name = hello()
    print(f"Hello, {user_name}!")
    rule_prime()
    while attempt < 3:
        result = prime_question()
        answer = user_answer()
        if answer == result:
            attempt += 1
            print('Correct!')
        else:
            print(f"{answer}  is wrong answer ;(. Correct answer was {result}\
            \nLet's try again, {user_name}!")
            raise SystemExit

    print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    main()
