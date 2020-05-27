import random
countries_cities = {"Austria": "Vienna", "Croatia": "Zagreb", "Spain": "Madrid", "Slovenia": "Ljubljana"}
def guesscapital():
    country = random.choice(list(countries_cities.keys()))
    while True:
        question = input("What's the capital of " + country + "?: ").lower()
        if question == countries_cities.get(country).lower():
            print("Congratulations")
            break
        else:
            print("try agaian")
guesscapital()