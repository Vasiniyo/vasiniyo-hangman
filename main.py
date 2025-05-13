from itertools import accumulate, tee
import os
import random
import re


def safe_input(p):
    try:
        return input(p)
    except KeyboardInterrupt as e:
        raise e
    except:
        return "%"


def get_hangman_states():
    base = "    |        "
    left = "    |       "
    footer = f"{base} |"
    empty_body = "    |\n" * 7
    return accumulate(
        [
            lambda h: h[:2] + [f"{base} |", f"{base}(_)", *[footer] * 3] + h[7:],
            lambda h: h[:4] + [f"{left} _|", f"{left}/ |"] + h[6:],
            lambda h: h[:4] + [f"{left} _|_", f"{left}/ | \\"] + h[6:],
            lambda h: h[:7] + [f"{left} /", f"{left}/"] + h[9:],
            lambda h: h[:7] + [f"{left} / \\", f"{left}/   \\"] + h[9:],
        ],
        lambda prev, f: f(prev),
        initial=f'    |{"-" * 18}\n    |/        |\n{empty_body} ___|{"_" * 18}\n  |{" " * 18}|'.splitlines(),
    )


possible_letters = "йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
hangman_states = list(get_hangman_states())
clear_screen = lambda: os.system("cls" if os.name == "nt" else "clear")
get_random_word = lambda: random.choice(words)

validate_input = lambda letter, used_letters: {
    letter in used_letters: f"Буква {letter} уже использовалась",
    len(letter) == 0: "Буква не может быть пустой!",
    len(letter) > 1: "Буква должна содержать только 1 символ!",
    letter not in possible_letters: ("Недопустимый символ!"),
}.get(True)


def start_new_game(words):
    def show_status():
        print(
            hangman_visual,
            " ".join(map(lambda r: r if r in guessed_letters else "*", secret_word)),
            f"Ошибки ({len(wrong_letters)}): " + ",".join(wrong_letters),
            sep="\n",
        )

    def update_screen():
        clear_screen()
        show_status()

    def get_valid_letter():
        while True:
            player_input = safe_input("Ваша буква: ").lower()
            validation_message = validate_input(
                player_input, guessed_letters | wrong_letters
            )
            if validation_message:
                update_screen()
                print(validation_message)
            else:
                return player_input

    secret_word = random.choice(words)
    hangman_generator = iter(hangman_states)
    guessed_letters, wrong_letters = set(), set()
    get_game_result = lambda: {
        guessed_letters == set(secret_word): "Вы выиграли",
        len(wrong_letters) == 5: f"Вы проиграли.\nБыло загадано слово '{secret_word}'",
    }.get(True)
    hangman_visual = "\n".join(next(hangman_generator))
    update_screen()
    while (game_result := get_game_result()) is None:
        player_input = get_valid_letter()
        if player_input in secret_word:
            guessed_letters.add(player_input)
        else:
            wrong_letters.add(player_input)
            hangman_visual = "\n".join(next(hangman_generator))
        update_screen()
    update_screen()
    print(game_result)


if __name__ == "__main__":
    try:
        with open("words.txt") as file:
            words = re.split(r"[ ,;\n]+", file.read())
        while safe_input("Начать новую игру? [Y/n]:").lower() == "y":
            start_new_game(words)
    except KeyboardInterrupt:
        print("Завершение игры.")
