# Functions
''' A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
In python a function is defined using def keyword.'''

def performOperation(num1, num2, operation):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2
print(performOperation(2, 3, 'sum'))

# Named Parameters
def performOperation(num1, num2, operation='sum'):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2
print(performOperation(2, 3))


def performOperation(num1, num2, operation='sum'):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2
print(performOperation(2, 3, 'multiply'))

# *arg
def performOperation(*args):
    print(args)
performOperation(1,2,3)

# **kwargs
def performOperation(*args, **kwargs):
    print(args)
    print(kwargs)
performOperation(1,2,3, operation='sum')
