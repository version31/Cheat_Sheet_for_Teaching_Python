# Python For Loops
# It's used for iterating over a sequence ( a list, a tuple, a dictionary, a set, or a string).
# The for loop does not require an indexing variable to set beforehand.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping Through a String
# strings are iterable objects
for x in "banana":
    print(x)

# The break Statement
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

# The continue Statement

for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() Function
for x in range(6):
    print(x)  # Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

for x in range(2, 6):
    print(x)

# [*] The range() function defaults to increment the sequence by 1,
# however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
    print(x)

# Else in For Loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# The pass Statement
for x in [0, 1, 2]:
    pass
# having an empty for loop like this, would raise an error without the pass statement
