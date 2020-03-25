# Python Conditions and If statements
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 33
b = 200

if b > a:
    print("b is greater than a")

# Indentation
# if b > a:
# print("b is greater than a")  # you will get an error

# elif and else

if b > a:

    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:  # You can also have an else without the elif:
    print("a is greater than b")

# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If ... Else
# This technique is known as Ternary Operators, or Conditional Expressions.
print("A") if a > b else print("B")
c # You can also have multiple else statements on the same line:

# And
a = 200
b = 33
c = 500
if a > b and c > a:  # if b < a < c:
    print("Both conditions are True")

# OR
if a > b or a > c:
    print("At least one of the conditions is True")

# Nested If
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# The pass Statement
# having an empty if statement like this, would raise an error without the pass statement
if b > a:
    pass
