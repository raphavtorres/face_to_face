import json

PATH_FILE = 'json.json'


class Person:
    CURRENT_YEAR = 2022

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_birth_year(self):
        return Person.CURRENT_YEAR - self.age
    

p1 = Person('Raphael', 19)
p2 = Person('Maristella', 18)
p3 = Person('Beck', 20)
bd = [vars(p1), p2.__dict__, vars(p3)]

# classe não serializável em json

def dump():
    with open(PATH_FILE, 'w', encoding='utf8') as file:
        print('DUMPING')
        json.dump(bd, file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    dump()
    