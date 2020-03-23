# Tuple
#  ordered and unchangeable

# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])
print(thistuple[-4:-1])

# Change Tuple Values
#  Tuples are unchangeable, or immutable as it also is called.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

    # Tuple Length
    thistuple = ("apple", "banana", "cherry")
    print(len(thistuple))

# Add Items
# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
thistuple[3] = "orange"  # This will raise an error

# Create Tuple With One Item
# To create a tuple with only one item, you have add a comma after the item, unless Python will not recognize the variable as a tuple.

thistuple = ("apple",)
print(type(thistuple))  # // <class 'tuple'>

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))  # // <class 'str'>

# Remove Items
# Note: You cannot remove items in a tuple.

del thistuple  # # The del keyword can delete the tuple completely:
print(thistuple)  # this will raise an error because the tuple no longer exists

# The del keyword can delete the tuple completely:
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)  # // ('a', 'b', 'c', 1, 2, 3)

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# Tuple Methods
# count()
# Returns the number of times a specified value occurs in a tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

# index()
# Searches the tuple for a specified value and returns the position of where it was found
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8) # // Search for the first occurrence of the value 8, and return its position:
print(x) # // 3