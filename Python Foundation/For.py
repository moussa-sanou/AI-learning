# For Loop
''' A For loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary,
a set, or a string)'''

myList = [1,2,3,4]
for item in myList:
    print(item)

# Using pass in a loop
animalLookup = {
    'a' : ['Antelope', 'Chakroman'],
    'b' : ['bear'],
    'c' : ['cat'],
    'd' : ['dog']
}
for letter, animals in animalLookup.items():
    pass

# Using continue in a loop
for letter, animals in animalLookup.items():
    if len(animals) > 1:
        continue
    print(f'Only one animal! {animals}')

# Using break statement in a loop
for letter1, animals1 in animalLookup.items():
    if len(animals1) > 1:
        print(f'Found {len(animals1)} animals: {animals1}')
        break
