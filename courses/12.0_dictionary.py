# Dictionary
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Accessing Items
x = thisDict["model"]
print(x)

x = thisDict.get("model")
print(x)

# Change Values
thisDict["year"] = 2018

# Loop Through a Dictionary
for x in thisDict:
    print(x)  # Print all key names

for x in thisDict:
    print(thisDict[x])  # Print all values

for x in thisDict.values():
    print(x)

x = thisDict.values()
print(x)  # // dict_values(['Ford', 'Mustang', 1964])

for x, y in thisDict.items():
    print(x, y)

# //
# brand Ford
# model Mustang
# year 1964

# Check if Key Exists
if "model" in thisDict:
    print("Yes, 'model' is one of the keys in the thisDict dictionary")

# Dictionary Length
print(len(thisDict))  # // 3

# Adding Items
thisDict["color"] = "red"

# Removing Items
thisDict.pop("model")

thisDict.popitem()  # removes the last inserted item

del thisDict["model"]

del thisDict
print(thisDict)  # this will cause an error because "thisDict" no longer exists.

thisDict.clear()

# Copy a Dictionary

newDict = thisDict.copy()

newDict = dict(thisDict)  # another way

# Nested Dictionaries
myFamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

# [*]
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(myFamily)

# The dict() Constructor
thisDict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisDict)  # // {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
