# [1] String Literals

print("Hello")
print('Hello')
a = "Hello"
print(a)

# [2] Multiline Strings

a = """Iran, also called Persia, 
and officially the Islamic Republic of Iran, is a country in Western Asia.
 With 83 million inhabitants, Iran is the world's 18th most populous country."""
print(a)

a = '''
Iran, also called Persia, is a country in Western Asia.
 With 83 million inhabitants,
 Iran is the world's 18th most populous country.
 '''
print(a)

# [3] Strings are Arrays
# [*] Python does not have a character data type
# [*] [Square brackets] {curly brace}

a = "Hello, Kourosh!"
print(a[1])

# [4] Slicing
print(a[2:5])  # //llo
print(a[-5:-2])  # //ros

# [5] String Length
# [*] All string methods returns new values. They do not change the original string.
print(len(a))  # // 15

# [6] String Methods
a.strip()
a.lower()
a.upper()
a.replace("H", "J")
a.split(",")

