#Экземпляры классов

#Инстанцировать класс в Python тоже очень просто:
class SomeClass(object):
    attr1 = 42

    def method1(self,x):
        return 2*x
obj = SomeClass()
print(obj.method1(6)) # 12
print(obj.attr1) # 42

#Можно создавать разные инстансы одного класса с заранее заданными параметрами с помощью инициализатора (специальный метод __init__)
#Для примера возьмем класс Point (точка пространства), объекты которого должны иметь определенные координаты:
class Point(object):
    def __init__(self,x,y,z):
        self.coord = (x,y,z)
p = Point(2,4,5)
p.coord #(2,4,5)