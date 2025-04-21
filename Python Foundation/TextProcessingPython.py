# Text processing in Python

test = '''Python is one of the most commonly used dynamic languages for many large organizations, including Google, 
Yahoo, and IBM. Supported on all major operating systems, it comes pre-installed on Macs, as well as most Linux 
and Unix-based systems. In this course, senior software engineer Ryan Mitchell guides you through all the essentials 
of learning and using Python. Learn how computers think, as well as how to install Python, pip, and Jupyter Notebook 
and the basics of writing a program. Explore variables and types, operators, functions, classes, objects, and more. 
Go over basic data types like ints and floats, Booleans, and strings. Deep dive into basic data structures, control 
flow, functions, classes, and objects. Find out how to handle errors and exceptions, as well as threads and processes. 
Plus, discover how to work with different types of files in Python, pass command-line arguments to your Python script, 
and create modules and packages.'''

def lowercase(text):
    return text.lower()

def removePunctuation(text):
    punctuations = ['.','-', ',', "'"]
    for punctuation in punctuations:
        text = text.replace(punctuation, '')
    return text

def removeNewlines(text):
    text = text.replace('\n', ' ')
    return text

def removeShortWords(text):
    return ' '.join(word for word in text.split() if len(word) > 3)

def removeLongWords(text):
    return ' '.join([word for word in text.split() if len(word) < 6])

processingFunctions = [lowercase, removePunctuation, removeNewlines, removeLongWords]
for fune in processingFunctions:
    text = fune(text)
print(text)