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

print('----------'*10)
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

print('----------'*10)
# *arg
def performOperation(*args):
    print(args)
performOperation(1,2,3)

print('----------'*10)
# **kwargs
def performOperation(*args, **kwargs):
    print(args)
    print(kwargs)
performOperation(1,2,3, operation='sum')

# locals()
print('----------'*10)
print('Print function using locals')
def performOperation(num1, num2, operation='sum'):
    print(locals())
performOperation(1,2,operation='multiply')

# Global
print('----------'*10)

message = 'some global data'
varA = 2
def function1(varA, varB):
    print(varA)
    print(message)
    print(locals())

def function2(varC, varB):
    print(varA)
    print(message)
    print(locals())

function1(1,2)
function2(3,4)