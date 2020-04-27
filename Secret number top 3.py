import random
import json
import datetime

secret = random.randint(1, 30)
attempts = 0

with open("score.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))
for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date") + " name: " + score_dict.get("name") + " Wrong guesses: " + score_dict.get("wrong_guesses"))

name = input("What's your name player?: ")
wrong_guesses = []
while True:
    guess = int(input("Guess the secret number (between 1 and 30) " + name + ": "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "name": name, "wrong_guesses" : wrong_guesses})
        with open("score.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))
        print(name + " You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed " + name + ": " + str(attempts))
        break
    elif guess > secret:
        print(name + " your guess is not correct... try something smaller")
    elif guess < secret:
        print(name + " your guess is not correct... try something bigger")
    else:
        print("algo fue mal")

    wrong_guesses.append(guess)
