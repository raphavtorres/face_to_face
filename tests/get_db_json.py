import json

from class_main import PATH_FILE, Person

with open(PATH_FILE, 'r', encoding='utf8') as file:
    people = json.load(file)
    p1 = Person(**people[0])
    p2 = Person(**people[1])
    p3 = Person(**people[2])

    print(p1.name, p1.age)
    print(p2.name, p2.age)
    print(p3.name, p3.age)
