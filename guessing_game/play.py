from card_types import vehicles, country
import inquirer
from random import choice

def game_type():
    card_type = [
            inquirer.List('type',
                            message="Select your card type:",
                            choices=['Vehicles', 'Country'],
                            ),
            ]
    answers = inquirer.prompt(card_type)
    return answers['type']

z = game_type()

if z == "Vehicles":
    x = choice(vehicles)
elif z == "Country":
    x = choice(country)

x.play()




