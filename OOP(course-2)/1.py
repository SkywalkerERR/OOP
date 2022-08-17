class Student:
    def __init__(self,name):
        self.name = name
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name


stud = Student('Sasha')
new_stud = Student('Kolya')
print(stud.name)
print(new_stud.name)