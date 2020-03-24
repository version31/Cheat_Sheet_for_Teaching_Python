# Tuple
#  ordered and unchangeable

# Access Tuple Items
thisTuple = ("apple", "banana", "cherry")
print(thisTuple[1])
print(thisTuple[-1])
print(thisTuple[2:5])
print(thisTuple[-4:-1])

# Change Tuple Values
#  Tuples are unchangeable, or immutable as it also is called.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Loop Through a Tuple
thisTuple = ("apple", "banana", "cherry")
for x in thisTuple:
    print(x)

# Check if Item Exists
thisTuple = ("apple", "banana", "cherry")
if "apple" in thisTuple:
    print("Yes, 'apple' is in the fruits tuple")

    # Tuple Length
    thisTuple = ("apple", "banana", "cherry")
    print(len(thisTuple))

# Add Items
# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
thisTuple[3] = "orange"  # This will raise an error

# Create Tuple With One Item
# To create a tuple with only one item, you have add a comma after the item, unless Python will not recognize the variable as a tuple.

thisTuple = ("apple",)
print(type(thisTuple))  # // <class 'tuple'>

# NOT a tuple
thisTuple = ("apple")
print(type(thisTuple))  # // <class 'str'>

# Remove Items
# Note: You cannot remove items in a tuple.

del thisTuple  # # The del keyword can delete the tuple completely:
print(thisTuple)  # this will raise an error because the tuple no longer exists

# The del keyword can delete the tuple completely:
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)  # // ('a', 'b', 'c', 1, 2, 3)

# The tuple() Constructor
thisTuple = tuple(("apple", "banana", "cherry"))
print(thisTuple)

# Tuple Methods
# count()
# Returns the number of times a specified value occurs in a tuple
thisTuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thisTuple.count(5)
print(x)

# index()
# Searches the tuple for a specified value and returns the position of where it was found
thisTuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thisTuple.index(8)  # // Search for the first occurrence of the value 8, and return its position:
print(x)  # // 3
