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
    return people[0]


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
            
            
