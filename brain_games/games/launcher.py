from brain_games.games.hello_user import say_hello


def game_launcher(game):
    game_rule = game.GAME_RULE
    attemp = 0
    user_name = say_hello()
    print(game_rule)
    while attemp < game.GAME_ROUNDS:
        question, correct_answer = game.get_game()
        print(question)
        answer = game.get_answer()
        if game.is_answer(correct_answer, answer):
            print('Correct!')
            attemp += 1
        else:
            print(f"{answer} is wrong answer ;(. "
                  f"Correct answer was {correct_answer}."
                  f"\nLet's try again, {user_name}!")
            raise SystemExit

    print(f"Congratulations, {user_name}!")
