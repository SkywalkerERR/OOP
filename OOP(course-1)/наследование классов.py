from tkinter import Tk, Button
#Наследование

class Verivication:

    def __init__(self,login,password):
        self.login = login
        self.password = password
        self.__lenPassword() #Недоступен для использования из вне, но доступен для использования в классе

    def __lenPassword(self):
        if len(self.password) < 8:
            raise ValueError ('слабый пароль')

    def save(self):
        with open('users','a') as r:
            r.write(f'{self.login,self.password}'+'\n')


class V2(Verivication): #Перенимаем его поведение и все его атрибуты
#класс будет пользоваться родительским __init__

    def __init__(self,login,password,age): #Переопределение __init__
        super().__init__(login, password)
        self.__save()
        self.age = age
    #метод не используется во вне, поэтому делаем приватным чтоб его можно было использовать только в классе
    def __save(self): #Переопределение
        with open('users') as r:
            for i in r:
                if f'{self.login,self.password}'+'\n' == i:
                    raise ValueError ('такой пользователь уже есть')
        #Код который будет записывать данные в файл
        super().save() #Будет выполнять метод save из родительского класса

    def show(self): #Добавление
        return self.login, self.password
x = V2('Nikola','123456789','33')

#Пример наследования классов
'''class My_app(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.geometry('400x400')
        self.setUI()
    def setUI(self):
        Button(self,text='OK').pack()
        
root = My_app()
root.mainloop()'''