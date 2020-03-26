# Syntax
# lambda arguments : expression
# [*] Use lambda functions when an anonymous function is required for a short period of time.


x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


# Why Use Lambda Functions?

def my_func(n):
    return lambda a: a * n


def my_func(n):
    return lambda a: a * n


myDoubler = my_func(2)

print(myDoubler(11))


def my_func(n):
    return lambda a: a * n


my_tripler = my_func(3)

print(my_tripler(11))


def my_func(n):
    return lambda a: a * n


my_doubler = my_func(2)
my_doubler = my_func(3)

print(my_doubler(11))
print(my_doubler(11))
