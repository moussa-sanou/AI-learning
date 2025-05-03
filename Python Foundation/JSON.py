import json
from json import JSONDecodeError, JSONEncoder

# Loading JSON
jsonString = '{"a": "apple", "b": "bear", "c":"cat"}'
json.loads(jsonString)
print(json.loads(jsonString))

# Dumping JSON
pythonDict = {"a": "apple", "b": "bear", "c":"cat"}
json.dumps(pythonDict)
print(json.dumps(pythonDict))

# Custom JSON Decoder
class Animal:
    def __init__(self, name):
        self.name = name

class AnimalEncoder(JSONEncoder):
    def default(self, o):
        if type(o) == Animal:
            return o.name
        return super().default(o)
pythonDict = {'a' : Animal('aardvark'), 'b': Animal('bear'), 'c': Animal('cat'),}
json.dumps(pythonDict, cls=AnimalEncoder)
print(json.dumps(pythonDict, cls=AnimalEncoder))