from random import shuffle
import json

from classes.Person import Person
from classes.Player import Player


FILE_PATH = 'json.json'

def header():
    print("WELCOME TO FACE TO FACE")
    nickname = input("Nickname >> ")
    return nickname


def create_people():
    people = []
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        objects = json.load(file)
        for obj in objects:
            people.append(Person(**obj))
    shuffle(people)
    return people


def game_logic(person, player):
    tips = person.tip

    for i in range(1, 6):
        print("\nLIFE AMOUNT =", player.life)
        print("\nTIP", i, tips[-1])
        tips.pop()
        
        guess = input("Guess >> ")

        if guess == person.name:
            print("You WON!")
            break
        else:
            player.loose_life()
            if (player.life == 0):
                print("You LOST!")
                break
            print(f"You're not {guess}")
            
            
def dump():
    p1 = Person("Beck", ['gay', 'randandan', 'moto', 'bigode', 'tpm'])
    p2 = Person("raphael", ['sensual', 'gaytbm', 'tpg', 'barba', 'maristella'])
    bd = [vars(p1), vars(p2)]
    with open(FILE_PATH, 'w', encoding='utf8') as file:
        json.dump(bd, file, ensure_ascii=False, indent=2)


def face_to_face():
    # name = header()
    player = Player(name="raphael")
    people = create_people()
    person = people[0]
    print("WELCOME,", player.name)
    game_logic(person, player)
