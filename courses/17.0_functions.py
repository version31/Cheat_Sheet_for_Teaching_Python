# Creating a Function
def my_function():
    print("Hello from a function")


# Calling a Function
my_function()


# Arguments
# Arguments are often shortened to args in Python documentations.
def print_full_name(fname):
    print(fname + " Khanjan")


my_function("Ali")
my_function("Amirhosein")


# Parameters or Arguments?
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that are sent to the function when it is called.

# Number of Arguments
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil")  # // error


# Arbitrary Arguments, *args
# [*] Arbitrary Arguments are often shortened to *args in Python documentations.
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# Keyword Arguments
# [*] The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# Arbitrary Keyword Arguments, **kwargs
# [*] Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.
def my_function(**kid):
    print("His last name is " + kid["lname"])


# Default Parameter Value

def my_function(country="Norway"):
    print("I am from " + country)


my_function()

my_function(fname="Tobias", lname="Refsnes")


# Passing a List as an Argument

def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# Return Values
def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


# The pass Statement

def my_function():
    pass


# Recursion
def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
