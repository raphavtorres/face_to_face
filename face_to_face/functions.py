from random import shuffle
import json

from classes.Person import Person


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


def test_guess(person, player, guess):
    if guess == person.name:
        player.life = 1000
    else:
        player.life = -20

    return player.life


def dump():
    p1 = Person("Person_1", ['1', '2', '3', '4', '5'])
    p2 = Person("Person_2", ['1', '2', '3', '4', '5'])
    bd = [vars(p1), vars(p2)]
    with open(FILE_PATH, 'w', encoding='utf8') as file:
        json.dump(bd, file, ensure_ascii=False, indent=2)
