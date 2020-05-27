import random
import json
import datetime
import operator

name = input("What's your name player?: ")

secret = random.randint(1, 30)
attempts = 0

with open("score.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

new_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]
for score_dict in new_score_list:
   score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}".format(
           score_dict.get("name"),
           (score_dict.get("attempts")),
           score_dict.get("date"),
           score_dict.get("secret"),
           score_dict.get("wrong_guesses"))

   print(score_text)


wrong_guesses = []
while True:
    guess = int(input("Guess the secret number (between 1 and 30) " + name + ": "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "name": name, "wrong_guesses" : wrong_guesses, "secret_number": secret})
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
