class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return self.__class__(self.name + other.name, 0)

    def __iter__(self):
        return self.name.__iter__()


c1 = Cat('Tom', 5)
c2 = Cat('Alisa', 3)
c3 = c1 + c2
print(c3.name)
print(c3.age)
print(type(c3))
print(dir(c3))
