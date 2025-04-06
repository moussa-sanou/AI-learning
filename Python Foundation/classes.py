''' Python is an object-oriented programming language.
A class in python is a blueprint for creating objects. It encapsulates data(attributes)
and behavior(methods) into a single unit. '''

class Dog:

    #init stands for initialization, and this function is called whenever an instance of a class is created.
    '''All classes have a function called init, which is always executed when the class is being initiated.'''
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ' says: Bark!')

my_dog = Dog('Rover')
my_dog.speak()
another_Dog = Dog('Fluffy')
another_Dog.speak()