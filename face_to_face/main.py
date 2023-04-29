from flask import Flask, render_template, request

from functions import create_people, test_guess, game_logic


app = Flask(__name__)


people = create_people()
people_name = []
for person in people:
    people_name.append(person.name)
person = people[0]
player, tips = game_logic(person)
list_cluster = [""]


@app.route('/', methods=['POST', 'GET'])
def index():
    life_amount = player.life
    player_name = player.name

    if request.method == 'POST':
        guess = request.form['people_slc']
        life_amount = test_guess(person, player, guess)
    return render_template(
        'index.html',
        people=people_name,
        life_amount=life_amount,
        player_name=player_name,
        tip_person=[]
    )


@app.route("/looselife/", methods=['POST'])
def index_2():
    try:
        tip = tips[0]
        tips.pop(0)
    except IndexError:
        tip = ""
    list_cluster.append(tip)
    if request.method == 'POST':
        player.loose_life()
        life_amount = player.life
        player_name = player.name

    return render_template(
        'index.html',
        people=people_name,
        life_amount=life_amount,
        player_name=player_name,
        tip_person=list_cluster
    )


if __name__ == '__main__':
    app.run(debug=True)
