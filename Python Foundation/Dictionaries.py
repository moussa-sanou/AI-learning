# Dictionaries
''' Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered, changeable and do not allow duplicates.'''

animals = {
    'a' : 'Dog',
    'b' : 'Cow',
    'c' : 'Chicken'
}
print(animals)
print(animals['a'])
print(animals['c'])

'''Add to the dictionary'''
animals['d'] = 'Horse'
print(animals)

'''Replace a value in the dictionary'''
animals['a'] = 'Antelope'
print('The dic after changing the value of the key __a__ : ',animals)

'''Only print the keys of the dictionary'''
print('Printed keys of the dic',animals.keys())

'''Print only the values of the dic'''
print(animals.values())
print('The values of this dic are : ', animals)

'''Print the keys of the dic into a list'''
print('The keys in a list : ', list(animals.keys()))

print('The length on this dic is: ', len(animals))

# Dictionaries comprehensions
animalsList = [('a', 'antelope'), ('b', 'bear'), ('c', 'cat'), ('d', 'dog')]
animals = {item[0]: item[1] for item in animalsList}
print(animals)
