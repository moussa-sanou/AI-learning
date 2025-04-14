# Python Conditions and If Statements
'''Python supports the use of logical conditions from mathematics:
    - Equals: a == b
    - Not Equals: a != b
    - Less than: a < b
    - Less than or equal to: a <= b
    - Greater than a > b
    Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly if "if statements" and loops '''

for n in range(1, 101):
    if n % 15 == 0:
        print('FizzBuzz')
    else:
        if n % 3 == 0:
            print('Fizz')
        else:
            if n % 5 == 0:
                print('Buzz')
            else:
                print(n)

print('----' * 20)

# Elif Statements
'''The elif keyword is python's way of saying "if the previous conditions were not true, then try this condition" '''
print('The fizz buzz challenge with elif')
for n in range(1, 101):
    if n % 15 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
print('----' * 20)
# Single line if Statement
print('One line if else statement')
n = 3
print('Fizz' if n % 3 == 0 else n)