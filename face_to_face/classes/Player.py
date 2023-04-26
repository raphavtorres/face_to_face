class Player():
    def __init__(self, name) -> None:
        self.__name = name
        self.__life = 100
        self.__tips_amount = 5

    @property
    def name(self):
        return self.__name
    
    @property
    def life(self):
        return self.__life
    
    @property
    def tips_amount(self):
        return self.__tips_amount
    
    def loose_life(self):
        self.__life -= 20
        self.__tips_amount =- 1
