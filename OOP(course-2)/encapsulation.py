#Инкапсуляция
#Все объекты в Python инкапсулируют внутри себя данные и методы работы с ними,
#предоставляя публичные интерфейсы для взаимодействия.

#Атрибут может быть объявлен приватным (внутренним) с помощью нижнего подчеркивания перед именем
class SomeClass:
    def _private(self):
        print('Это внутренний метод объекта')
obj = SomeClass()
obj._private()

#Если поставить перед именем атрибута два подчеркивания, к нему нельзя будет обратиться напрямую.

class SomeClass:
    def __init__(self):
        self.__param = 42 #Защищенный атрибут

obj = SomeClass()
obj.__param #Выдает ошибку
obj._SomeClass__param #Обходной путь - выведет 42

#Кроме прямого доступа к атрибутам (obj.attrName),
# могут быть использованы специальные методы доступа (геттеры, сеттеры и деструкторы):
class SomeClass():
    def __init__(self,value):
        self.value = value
    def getvalue(self):
        return self.value
    def setvalue(self,value):
        self._value = value
    def delvalue(self):
        del self.value
    value = property(getvalue,setvalue,delvalue,'Свойство Value')

obj = SomeClass(42)
print(obj.value)
obj.value = 43

#__getattr__
# __setattr__
# __delattr__s
class SomeClass:
    attr1 = 41

    def __getattr__(self, attr):
        return attr.upper()
obj = SomeClass()
print (obj.attr1) #41
print (obj.attr2) #ATTR2

