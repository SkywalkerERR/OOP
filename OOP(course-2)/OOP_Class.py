
#Создание класса
class SomeClass(object):
    # поля и методы класса SomeClass

#Классы-родители перечисляются в скобках через запятую
class SomeClass(ParentClass1,PArentClass2,...):
    # поля и методы класса SomeClass

#Свойства классов устанавливаются с помощью простого присваивания
class SomeClass(object):
    attr1 = 42
    attr2 = 'Hello,world'

#Методы объявляются как простые функции
class SomeClass(object):
    def method1(self,x):
        # код метода


#Динамическое изменение классов
class SomeClass(object):
    pass
def squareMethod(self,x):
    return x*x

SomeClass.square = squareMethod
obj = SomeClass()
obj.square(5)


#Статистические и классовые методы

#Статистический:
#@staticmethod
class SomeClass(object):
    @staticmethod
    def hello():
        print('Hello world!') #У них нет обязательных параметров-ссылок вроде self.
        #Доступ к таким методам можно получить как из экземпляра класса, так и из самого  класса.
SomeClass.hello() #Hello world!
obj.SomeClass()
obj.hello() #Hello world!

#Классовый:
#@classmethod
class SomeClass(object):
    @classmethod
    def hello(cls):
        print('Hello, class {}'.format(cls.__name__))

SomeClass.hello() # Hello, class SomeClass
