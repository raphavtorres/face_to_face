import json

from classes.Player import Player
from classes.Person import Person
from functions import header, create_people, game_logic, FILE_PATH


def dump():
    p1 = Person("Beck", ['gay', 'randandan', 'moto', 'bigode', 'tpm'])
    p2 = Person("raphael", ['sensual', 'gaytbm', 'tpg', 'barba', 'maristella'])
    bd = [vars(p1), vars(p2)]
    with open(FILE_PATH, 'w', encoding='utf8') as file:
        json.dump(bd, file, ensure_ascii=False, indent=2)


def face_to_face():
    name = header()
    player = Player(name)
    person = create_people()
    print("WELCOME,", player.name)
    game_logic(person, player)


if __name__ == '__main__':
    # dump()
    face_to_face()
