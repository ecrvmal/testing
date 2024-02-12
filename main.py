class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.__subject = subject

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


t = Teacher(name='Ivan', subject='Math', age=23)

# t.get_age

class Digit:
    def __init__(self, num):
        self.num = num

    def plus(self,b):
        return self.num + b


# vary = Digit(5)
# print(vary.plus(7))

