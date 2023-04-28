import json
from flask import Flask, render_template

from functions import face_to_face, dump, create_people
from classes.Player import Player


def game_logic_2(person):
    player = Player(name="raphael")
    tips = person.tip

    for i in range(1, 6):
        """ print("\nLIFE AMOUNT =", player.life) """
        print("\nTIP", i, tips[-1])
        tips.pop()
        
        """ guess = input("Guess >> ") """

        """ if guess == person.name:
            print("You WON!")
            break
        else:
            player.loose_life()
            if (player.life == 0):
                print("You LOST!")
                break
            print(f"You're not {guess}") """

    return player, tips


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    people = create_people()
    people_name = []
    for person in people:
        people_name.append(person.name)
    person = people[0]
    player, tips = game_logic_2(person)

    return render_template('index.html', people=people_name, life_amount=player.life, player_name=player.name, tip_person=tips)


if __name__ == '__main__':
    # dump()
    app.run(debug=True)
    # face_to_face()
