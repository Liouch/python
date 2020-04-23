secret = 1

guess = input("Guess the secret number: ")

if int(guess) == secret:
    print("Congratulations")
else:
    print("Wrong! Sorry")
