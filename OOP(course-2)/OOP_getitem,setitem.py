#__getitem__
#__setitem__

#Представьте класс, который моделирует здание.
#Данные о здании включают в себя ряд атрибутов, в том числе описания компаний, занимающих каждый этаж:

#Без использования __getitem__у нас был бы такой класс:

class Building(object): # Здание
    def __init__(self,floors): # [None],[None],[None],[None] - типо 4 пустых этаж
        self.floors =  [None] * floors # Список из 4 пустых значений

    def occupy(self,floor_number,data): # Функция занятия этажей
        self.floors[floor_number] = data #этаж[намер этажа] = предприятие
        # т.е [None][Какой из None'ов выбираем] = значение

    def get_floor_data(self,floor_number): #Выводим информацию об этаже
        return self.floors[floor_number]

b = Building(4)
b.occupy(0,'Магазин')
b.occupy(1,'Салон-Красоты')
b.occupy(2,'Парикмахерская')
print(b.get_floor_data(1))

#Однако мы могли бы использовать __getitem__(и его аналог __setitem__)
# чтобы сделать использование класса Building более «приятным».

class Bulding1(object):
    def __init__(self,floors):
        self.floors = [None] * floors
    def __setitem__(self, floor_number, data): # тут мы создаем что-то типо словаря со значениями
        self.floors[floor_number] = data # выбираем этаж - присваиваем предприятие на нём
    def __getitem__(self, floor_number): # тут мы получаем значение из словаря
        return self.floors[floor_number]

bulding1 = Bulding1(4)
bulding1[0] = 'Магазин'
bulding1[1] = 'Салон-Красоты'
bulding1[2] = 'Парикмахерская'
print(bulding1[1])
