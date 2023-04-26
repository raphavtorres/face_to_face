from random import shuffle

class Person():
    def __init__(self, name, tip1, tip2, tip3, tip4, tip5) -> None:
        self.__name = name
        self.__tips = [tip1, tip2, tip3, tip4, tip5]

    @property
    def name(self):
        return self.__name
    
    @property
    def tip(self):
        shuffle(self.__tips)
        return self.__tips
