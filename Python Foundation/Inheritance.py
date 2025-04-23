# Inheritance
'''Inheritance allow us to define a class that inherits all the methods and properties from
another class.
Parent class is the class being inherited from, also called based class.
Child class is the class that inherits from another class, also called derived class. '''

class Dog:
    legs = 4
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + 'says: Bark:')

    def getLegs(self):
        return self.legs

class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says: Yap yap')

    def wagTail(self):
        print('Vigorous wagging!')

dog = Chihuahua('Roxy')
dog.speak()
dog.wagTail()

# Extending built-in classes
class UniqueList(list):
    def append(self, item):
        if item in self:
            return
        super().append(item)

uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)

print(uniqueList)