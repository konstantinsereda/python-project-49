from brain_games.answers import hello, rule_even, user_answer
from brain_games.questions import even_question


def main():
    user_name = hello()
    print(f"Hello, {user_name}!")
    rule_even()
    attempt = 0
    # if even_question() == user_answer():
    #     print(answer)
    #     print('Correct!')
    #     attempt += 1
    # else:
    #     if answer == 'yes':
    #         print("'yes' is wrong answer ;(. Correct answer was 'no'.")
    #     else:
    #         print("'no' is wrong answer ;(. Correct answer was 'yes'.")
    #
    # print(attempt)
    while attempt < 3:
        true_answer = even_question()
        answer = user_answer()
        if true_answer == answer:
            attempt += 1
            print('Correct!')
        else:
            if answer == 'yes':
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\
                      \nLet's try again, {user_name}!")
                raise SystemExit
            else:
                print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\
                      \nLet's try again, {user_name}!")
                raise SystemExit
    print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    main()
