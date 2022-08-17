#Наследование

#Стандартное одиночное наследование

class Mammal():
    className = 'Mammal'

class Dog(Mammal):
    species = 'Canis Lupus'

dog = Dog()
print(dog.className) # Mammal

#Множественное наследование

class Horse():
    isHorse = True

class Donkey():
    isDonkey = True

class Mule(Horse,Donkey):
    isMule = True
mule = Mule()
print(mule.isHorse) # True
print(mule.isDonkey) # True

#организации межклассового взаимодействия –
# ассоциация (агрегация или композиция), при которой один класс является полем другого.

#Пример композиции:

class Salary:
    def __init__(self,pay):
        self.pay = pay

    def getTotal(self):
        return (self.pay*12)

class Employee:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = Salary(self.pay)

    def annualSalary(self):
        return "Total: " + str(self.salary.getTotal() + self.bonus)

employee = Employee(100,10)
print(employee.annualSalary())

#Пример агрегации:

class Salary(object):
    def __init__(self, pay):
        self.pay = pay

    def getTotal(self):
        return (self.pay * 12)

class Employee(object):
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annualSalary(self):
        return "Total: " + str(self.pay.getTotal() + self.bonus)

salary = Salary(100)
employee = Employee(salary, 10)
print(employee.annualSalary())