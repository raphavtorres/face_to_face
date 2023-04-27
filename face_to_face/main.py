from classes.Player import Player
from functions import header, create_people, show_tip


def face_to_face():
    name = header()
    player = Player(name)
    print(player.name)
    person = create_people()
    print(person)
    show_tip(person)


if __name__ == '__main__':
    face_to_face()
