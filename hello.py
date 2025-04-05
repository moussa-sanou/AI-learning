# Print hello world
print('Hello, world')

# Defining a variable
# Integer
x = 5
print('this is an integer', x)

# String
name = 'Sami'
print('this is a string' , name)

# Numbers in python
# Float
grade = 3.2336
print('this is a float' , grade)

#Booleans
# Defined by true and false

# Data Structures
#Lists
# One dimensional list
my_list = [1, 2, 3, 4]
print('This is a list',my_list)

my_list = ['list', 'of', 'strings']
print(my_list)

# List with different data types
my_list = [1, 'list', False, []]
print(my_list)

# Multi dimensional list
my_list = [[1,2,3], [False, True],[]]
print(my_list)
print(len(my_list))

# Sets
my_set = {1,2,3,4,5}
print(my_set)
print(len(my_set))

# Tuples
my_tuple = (1,2,3)
print(my_tuple)
print(len(my_list))

''' Why use Tuples?
They're efficient 
Good for storing lots of little things, like x,y coordinates'''

# Dictionaries
my_dictionary = {'apple' : 'A red fruit',
                 'bear' : 'A scary animal'}
print(my_dictionary)
print(my_dictionary['apple'])

# Sets and Dictionaries
''' Both are defined with curly brackets
    Sets have a unique values, dictionaries have unique keys
    The order doesn't matter '''

# Functions
print('This is an example of a function')
def multiplyByThree(val):
    return 3 * val
print('4 * 3 = ', multiplyByThree(4))

def multiply(val1, val2):
    return val1 * val2
print('Here is the result of multiplying val1 and val2', multiply(5, 10))

'''A function sometime doesn't need the return statement'''
a = [1, 2, 3]

def appendFour(mylist):
    mylist.append(4)
appendFour(a)
print(a)



