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
