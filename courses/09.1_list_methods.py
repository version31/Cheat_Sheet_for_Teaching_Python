list = [1, 2, 3, 49, -4, 0]

list.sort()  # Sorts the list
list.reverse()  # Reverses the order of the list
list.append(66)  # Adds an element at the end of the list
new_list = list.copy()  # Returns a copy of the list
list.count(1)  # Returns the number of elements with the specified value
list.extend([])  # Add the elements of a list (or any iterable), to the end of the current list
print(list.index(-4))  # Returns the index of the first element with the specified value
list.insert(0, 90)  # Adds an element at the specified position
list.pop(2)  # Removes the element at the specified position
list.remove(-4)  # Removes the item with the specified value
list.clear()  # Removes all the elements from the list




# append()
# Adds an element at the end of the list
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)  # //['apple', 'banana', 'cherry', ["Ford", "BMW", "Volvo"]]

# clear()    
# Removes all the elements from the list

# copy()    
# Returns a copy of the list

# count()    
# Returns the number of elements with the specified value
fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = fruits.count(9)
print(x)  # // 2

# extend()    
# Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)  # //['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)  # //['apple', 'banana', 'cherry', 1, 4, 5, 9]

# index()    
# Returns the index of the first element with the specified value
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)  # //3 # Note: The index() method only returns the first occurrence of the value.

# insert()    
# Adds an element at the specified position

# pop()    
# Removes the element at the specified position

# remove()    
# Removes the item with the specified value

# reverse()    
# Reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)  # //['cherry', 'banana', 'apple']

# sort()    
# Sorts the list
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)  # // ['BMW', 'Ford', 'Volvo']

cars.sort(reverse=True)
print(cars)  # // ['Volvo', 'Ford', 'BMW']


# A function that returns the length of the value: # todo Browse after function
def myFunc(e):
    return len(e)


cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)  # // ['VW', 'BMW', 'Ford', 'Mitsubishi']


def myFunc(e):
    return e['year']


cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

print(cars)


# // [{'car': 'Mitsubishi', 'year': 2000}, {'car': 'Ford', 'year': 2005},{'car': 'VW', 'year': 2011}, {'car': 'BMW', 'year': 2019}]


# A function that returns the length of the value:
def myFunc(e):
    return len(e)


cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)  # // ['Mitsubishi', 'Ford'', 'BMW', 'VW']
