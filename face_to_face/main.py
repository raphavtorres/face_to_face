from classes.Player import Player
from classes.Person import Person
from functions import header
from random import shuffle

def create_people():
    p1 = Person('Beck', "branco(a)", 'alto(a)', 'faz facul', 'randandan', 'grau')
    p2 = Person('Alemão', "branco(a)", 'baixo(a)', 'não faz facul', 'kart', 'apêndice')
    p3 = Person('Maciel', "moreno(a)", 'baixo(a)', 'não faz facul', 'amaciente', 'verdin')

    people = [p1, p2, p3]
    shuffle(people)
    return people[0]

def show_tip(person):
    tips = person.tip

    for i in range(1, 5):
        print("TIP", i, tips[-1])
        tips.pop()
        
        guess = input("Guess >> ")
        if guess == person.name:
            print("You won!")
        else:
            print(f"You're not {guess}")


def face_to_face():
    name = header()
    player = Player(name)
    print(player.name)
    person = create_people()
    show_tip(person)

    

if __name__ == '__main__':
    face_to_face()

