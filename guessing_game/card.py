import os

class Card():
    def __init__(self, name) -> None:
        self._name = name
        self._tips = []
        # self._life = 5

    @property
    def name(self):
        return self._name

    @property
    def tips(self):
        return self._tips
    
    def add_tips(self, *tips):
        for tip in tips:
            self._tips.append(tip)

    # def lose_file(self, value=1):
    #     return self._life - value
    
    def print_tips(self, z):
        os.system("cls")
        print(f'Type #{z+1}: {self.tips[z]}')
        
    def verify_answer(self, answer, life):
        if answer == self.name:
            print("Congrats buddy!! You won!")
            quit()
        else:
            life -= 1
            

    def play(self):
        z = 0
        life = 5
        while life > 0:
            self.print_tips(z)
            z += 1
            answer = str(input("Input your answer>> ")).capitalize()
            self.verify_answer(answer, life)