import json

class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards



kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4)

messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67, red_cards=0)

# Vamos a probar desde aqui
with open("players.txt", "r") as players_file:
    players_list = json.loads(players_file.read())
def new_player():
    first_name = input("Name of the player: ")
    last_name = input("Last name of the player: ")
    height_cm = input("Height in cm of the player: ")
    weight_kg = input("Weight in kg of the player: ")
    type_of_player = input("Type basketball or football player?: ")

    if type_of_player == "basketball":
        points = input("Points of the player: ")
        assists = input("Assists of the player: ")
        rebounds = input("Rebounds of the player: ")
        new_player = BasketballPlayer(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg, points=points, rebounds=rebounds, assists=assists)

    elif type_of_player == "football":
        goals = input("goals of the player: ")
        yellow_cards = input("yellow cards of the player: ")
        red_cards = input("red cards of the player: ")
        new_player = FootballPlayer(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg, goals=goals, yellow_cards=yellow_cards, red_cards=red_cards)
    else:
        print("algo fue mal")

    players_list.append(new_player)
    with open("players.txt", "w") as players_file:
        for players in players_list:
            players_file.write(json.dumps(players.__dict__))
    print(players_list)

new_player()
if __name__ == "__main__":
    new_player()







