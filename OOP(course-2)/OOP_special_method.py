#Специальные методы

#Объект как функция
#Объект можно вызвать с параметрами, как функцию
#__call__

class Multiplier:
    def __call__(self,x,y):
        return x*y
multiply = Multiplier()
multiply(19,19) #361
multiply.__call__(19,19)


#Имитация контейнеров
#__len__
#Длинна спискового значения
class Collection:
    def __init__(self,list):
        self.list = list

    def __len__(self):
        return len(self.list)
collection = Collection([1,2,3])
len(collection)

#Имитация числовых типов
class SomeClass:
    def __init__(self,value):
        self.value = value
    def __mul__(self, number):
        return self.value * number

obj = SomeClass(2)
print(obj*100)