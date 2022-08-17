from datetime import datetime as dt

class Player:

    __LVL, __HEALTH = 1, 100 # константы/свойства
    __slots__ = ['__lvl','__health','__born']

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = dt.now()

    @property # Декоратор
    def lvl(self): #геттер
        return self.__lvl

    @lvl.setter # Декоратор
    def lvl(self,number): #сеттер
        self.__lvl += Player.__typeTest(number)

    @classmethod
    def set_cls_field(cls,lvl=1,health=100):
        cls.__LVL = Player.__typeTest(lvl)
        cls.__HEALTH = Player.__typeTest(health)

    @staticmethod
    def __typeTest(value):
        if isinstance(value,int): # если value является int
            return value
        else:
            raise TypeError ('Must be int')
x = Player()

print(x.lvl)
x.lvl = 5
print(x.lvl)