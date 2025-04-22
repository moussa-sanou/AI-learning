# Classes and Objects
'''Python is an object-oriented programming language.
Almost everything in Python is an object, with is properties and methods.
A Class is like an object constructor, or a blueprint for creating objects.'''

# Instance Attributes
class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ' says: Bark')

myDog = Dog('Kakou')
print(myDog.name)
print(myDog.legs)


# Static Attributes
class Dog:
    legs = 4
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' says: Bark')
print(Dog.legs)
print('------' * 10)

# Static and instance methods
class WordSet:
    def __init__(self):
        self.words = set()

    def addText(self, text):
        text = self.cleanText(text)
        for word in text.split():
            self.words.add(word)

    def cleanText(self, text):
        # changing functions
        text = text.replace('!', '').replace('.', '').replace(',','').replace('','')
        return text.lower()

wordset = WordSet()
wordset.addText('Hi, I\'m Sami! Here is a sentence I want to add!')
wordset.addText('Here is another sentence I want to add.')
print(wordset.words)



