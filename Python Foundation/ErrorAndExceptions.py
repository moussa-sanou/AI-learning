# Errors and Exceptions
''' Exceptions, when used correctly, are like a secondary layer of code'''
import time


def causeError():
    try:
        return 1/0
    except Exception as e:
        return e
print(causeError())
print('-------' * 10)

def causeError():
    try:
        return 1/0
    except Exception:
        print('There was some sort of error')
causeError()
print('-------' * 10)

# Finally
def causeError():
    try:
        return 1/0
    except Exception:
        print('There was some sort of error')
    finally:
        print('This will always execute!')
causeError()
print('-------' * 10)

def causeError():
    start = time.time()
    try:
        time.sleep(0.5)
        return 1/0
    except Exception:
        print('There was some sort of error')
    finally:
        print(f'Function took {time.time() - start} second to execute')
causeError()
print('-------' * 10)

# Catching exceptions by type

def causeError():
    try:
        return 1 + 'a'
    except TypeError:
        print('There was a type error!')
    except ZeroDivisionError:
        print('There was a zero division error!')
    except Exception:
        print('There was some sort of error')
causeError()
print('-------' * 10)

# Custom Decorators

def handleException(fune):
    def wrapper():
        try:
            fune()

        except TypeError:
            print('There was a type error!')

        except ZeroDivisionError:
            print('There was a zero division error!')
        except Exception:
            print('There was some sort of error')

    return wrapper

@handleException
def causeError():
    return 1/0

causeError()

print('-------' * 10)

# Raising Exceptions

@handleException
def raiseError(n):
    if n == 0:
        raise Exception()
    print(n)
raiseError()

print('-------' * 10)

# Customer Exceptions
'''EXCEPTION CLASSES
- Keep code clean and organized
- Exception classes act as documentation 
- They separate common expected errors from issues that require developer attention'''

class CustomException(Exception):
    pass

def causeError():
    raise CustomException('You called the causeError function!')
causeError()

print('-------' * 10)

# Adding Attributes
class HttpException(Exception):
    statusCode = None
    message = None
    def __init__(self):
        super().__init__(f'Status code: {self.statusCode} and message is: {self.message}')

class NotFound(HttpException):
    statusCode = 404
    message = 'Resource not found'

class ServerError(HttpException):
    statusCode = 500
    message = 'The server messed up'

def raiseServerError():
    raise ServerError()
raiseServerError()