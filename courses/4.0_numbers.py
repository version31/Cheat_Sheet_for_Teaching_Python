import random

# [1] Python Numbers
x = 1  # int  (*)unlimited length.
y = 2.8  # float
y2 = 35e3  # (*)Float can also be scientific numbers with an "e" to indicate the power of 10
y3 = 12E4
y4 = -87.7e100
z = 3 + 5j  # complex

# [2] Type Conversion
x, y, z = 1, 1.1, 1j
a = float(x)
b = int(y)
c = complex(x)

# [3] Random Number
print(random.randrange(1, 10))
