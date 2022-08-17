
class Purse:

    def __init__(self,valuta,name='Unknown'):
        if valuta not in ('USD','EUR'):
            raise ValueError
        self.__money = 0.00
        self.valuta = valuta
        self.name = name

    def top_up_balance(self,howmany): # пополняем
        self.__money =  self.__money + howmany
        return howmany

    def top_down_balance(self,howmany): # тратим
        if self.__money - howmany < 0:
            print('Недостаточно средств')
            raise ValueError ('Недостаточно средств')
        self.__money = self.__money - howmany
        return howmany


    def perevod(self,howmany,name): # САМ СДЕЛАЛА НА ПЕРЕВОД МЕТОД
        if self.__money - howmany < 0:
            print('Недостаточно средств')
        self.__money = self.__money - howmany
        name.__money += howmany


    def info(self):
        print(self.__money)

    def __del__(self): # деструктор
        print('Кошелек удален')

x = Purse('USD')
y = Purse('USD','Bill')

x.top_up_balance(10)
y.top_up_balance(x.top_down_balance(3)) #ПОПОЛНИТЬ Y СПИСАВ СРЕДСТВА С Х

x.info()
y.info()

