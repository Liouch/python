import random
import json
import datetime

def play_game(level="easy"):
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()
    name = input("What's your name player?: ")
    wrong_guesses = []

    while True:
        guess = int(input("guess the secret number (1-30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "name": name,
                               "wrong_guesses": wrong_guesses, "secret_number": secret})
            with open("score.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))
            print(name + " You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed " + name + ": " + str(attempts))
            break
        elif guess > secret and level == "easy":
            print(name + " your guess is not correct... try something smaller")
        elif guess < secret and level == "easy":
            print(name + " your guess is not correct... try something bigger")
        else:
            print("try again")

def get_score_list():
    with open("score.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list

def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k["attempts"])[:3]
    return top_score_list

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    if selection.upper() == "A":
        level = input("choose your level (easy/hard): ")
        play_game(level=level)
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
        else:
            break