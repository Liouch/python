
user_name = input("What's your name?: ")
user_mood = input("How are you feeling today " + user_name+"?:")
mood = user_mood

if mood == "happy":
    print("it is great to see you happy!")
elif mood == "nervous":
    print("take a deep breath 3 times.")
elif mood == "sad":
    print("you little piece of shit, cheer up")
elif mood == "excited":
    print("just don't be excited")
elif mood == "relaxed":
    print("that's good mate!")
else:
    print("I don't recognize this mood")