from abc import *


class SchoolMembers(metaclass=ABCMeta):
    '''Представляет любого человека в школе.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))

    @abstractmethod
    def tell(self):
        '''Вывести информацию.'''
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMembers):
    '''Представляет преподавателя.'''
    def __init__(self, name, age, salary):
        SchoolMembers.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMembers.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))


class Student(SchoolMembers):
    '''Представляет student.'''
    def __init__(self, name, age, marks):
        SchoolMembers.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))

    def tell(self):
        SchoolMembers.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))


teacher = Teacher('Lidia Pavlovna', 2000, 1400)
student = Student('Andrey', 18, 4)

print()
print()

members = [teacher, student]

for memb in members:
    memb.tell()





