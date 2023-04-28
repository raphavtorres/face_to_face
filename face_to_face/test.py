import json
from flask import Flask, render_template, request, redirect

from functions import face_to_face, dump, create_people
from classes.Player import Player


def game_logic_2(person):
    player = Player(name="raphael")
    tips = person.tip

    for i in range(1, 6):
       
        print("\nTIP", i, tips[-1])
        tips.pop()

    return player, tips


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    people = create_people()
    people_name = []
    for person in people:
        people_name.append(person.name)
    person = people[0]
    player, tips = game_logic_2(person)

    if request.method == 'POST':
        task_content = request.form['people_slc']
        print(task_content)

    return render_template('test.html', people=people_name, life_amount=player.life, player_name=player.name, tip_person=tips)


if __name__ == '__main__':
    app.run(debug=True)
