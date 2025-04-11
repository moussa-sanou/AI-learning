# Sets
''' Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in python used to store collections of data, the other 3 are,
List, Tuple, and Dictionary. Sets can only contain unique values. '''

mySet = {'a', 'b', 'c'}
print(mySet)

'''Set can only contains unique value'''
mySet ={'a', 'a', 'b', 'b', 'c'}
print(mySet)

mySet.add('d')
print(mySet)
print('The size of the set is: ',len(mySet))

while len(mySet):
    print(mySet.pop())

# Properties of Sets
''' Declared with curly brackets{}
    All elements are unique
    The order doesn't matter'''
