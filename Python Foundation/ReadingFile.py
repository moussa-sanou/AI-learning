
f = open('10_01_file.txt', 'r')
print(f)
print('----------' * 10)

# Read only one line in the file
print(f.readline())
print('----------' * 10)

# Read all the lines in the file
print(f.readlines())
print('----------' * 10)

# Print the file text in a more readable form
f = open('10_01_file.txt', 'r')
for line in f.readlines():
    print(line)
print('----------' * 10)

# Remove the white spaces within the text
f = open('10_01_file.txt', 'r')
for line in f.readlines():
    print(line.strip())
print('----------' * 10)

# Writing Files

'''Creates a file'''
f = open('10_01_output.txt', 'w')
print(f)

'''Write in the file'''
f.write('Line 1\n')
f.write('Line 2\n')
f.close()

'''Appending Files'''
f = open('10_01_output.txt', 'a')
f.write('Line 3\n')
f.write('Line 4\n')
f.close()
print('----------' * 10)

# Another way of appending a file

with open('10_01_output.txt', 'a') as f:
    f.write('some stuff\n')
    f.write('some other stuff\n')
print(f)
