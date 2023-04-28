from random import shuffle

class Person():
    def __init__(self, _Person__name, _Person__tips):
        self.__name = _Person__name
        self.__tips = _Person__tips

    @property
    def name(self):
        return self.__name
    
    @property
    def tip(self):
        shuffle(self.__tips)
        return self.__tips
