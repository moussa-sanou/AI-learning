# List slicing
print('This is an example of list slicing')
myList = [1,2,3,4,5]
print(myList[3:])
print(myList[0:6:2])
print(myList[0:6:3])
print(myList[::2])

for i in range(100):
    print(i)

myList = list(range(100))
print(myList[::10])
print()

# Modifying List
print('This is an example of list modification')
myList = [1,2,3,4]
myList.append(5)
print(myList)

myList.insert(3, 'a new value')
print(myList)
myList.remove('a new value')
print(myList)