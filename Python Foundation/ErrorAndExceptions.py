# Errors and Exceptions
''' Exceptions, when used correctly, are like a secondary layer of code'''

def causeError():
    try:
        return 1/0
    except Exception as e:
        return e
print(causeError())


def causeError():
    try:
        return 1/0
    except Exception:
        print('There was some sort of error')
causeError()

# Finally

def causeError():
    try:
        return 1/0
    except Exception:
        print('There was some sort of error')
    finally:
        print('This will always execute!')
causeError()