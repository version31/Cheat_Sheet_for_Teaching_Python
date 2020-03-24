# [1] Creating Variables
a = 5
b = 3.14
c = -1
d = 0
st = "Amirhosein"
t = True
f = False

# double quotes & single quotes are same:
x = "Ali"
x = 'Ali'

# [2] Variable Names
myVar = "Ali"
my_var = "Ali"
_my_var = "Ali"
myVar = "Ali"
MYVAR = "Ali"
myVar2 = "Ali"

# Illegal variable names:
# 2myVar = "Ali"
# my-var = "Ali"
# my var = "Ali"
# $ali = 5
# al.i = 10

# ( ali === Ali) // False
# python is case-sensitive


# [3] Assign Value to Multiple Variables
x, y, z = "Ali", "Kourosh", "Amirhosein"

# [*] = is Assign . it's not equal

# [?]
x = y = z = "Khanjan"
print(x)  # // ?
print(y)  # // ?
print(z)  # // ?

# [?]
a = 5
b = 3
a = 4
a = a + b
print(a)  # // ?

# [4] Output Variables
x = "best teacher"
print("Ali is " + x)  # + is combine operator

x = "Amirhosein is "
y = "energetic"
z = x + y
print(z)

x = 5
y = 10
print(x + y)  # + is mathematical operator here

# [*]
x = 5
y = "Kourosh"
print(x + y)  # //Error

# [5] Global Variables todo I'll describe that after functions
x = "cool"


def myfunc():
    print("Amirhosein is " + x)


myfunc()

# [*]
y = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()
print("Python is " + x)


# [6] The global Keyword

def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)

# change a global variable inside a function

x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
