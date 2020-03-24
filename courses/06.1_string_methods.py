# [1] methods
txt = "amirhosein will be rich this year."

txt.capitalize()
# txt = "2 farvardin" // ???

txt.casefold()
# txt = Amirhosein Is a Rich Man
# txt = 'ß'
# txt.casefold() == txt.lower()   // ???

txt.center()
# string.center(length, character:optional)
# txt.center(20)
# txt.center(20, "*")

txt.count()
# string.count(value, start:optional, end:optional)
# txt.count("amirhosein")
# txt.count("amirhosein" , 2 , 100)


txt.encode()
# string.encode(encoding=encoding:optional(UTF-8), errors=errors:optional)
# txt = "نیستانی"
# 'backslashreplace'	- uses a backslash instead of the character that could not be encoded
# 'ignore'	- ignores the characters that cannot be encoded
# 'namereplace'	- replaces the character with a text explaining the character
# 'strict'	- Default, raises an error on failure
# 'replace'	- replaces the character with a questionmark
# 'xmlcharrefreplace'	- replaces the character with an xml character
#
# txt = "My name is åli"
#
# print(txt.encode(encoding="ascii",errors="backslashreplace"))
# print(txt.encode(encoding="ascii",errors="ignore"))
# print(txt.encode(encoding="ascii",errors="namereplace"))
# print(txt.encode(encoding="ascii",errors="replace"))
# print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
# print(txt.encode(encoding="ascii",errors="strict"))

txt.endswith()
# string.endswith(value, start:optional, end:optional):bool
# x = txt.endswith(".")
# x = txt.endswith("this year.")
# print(x)

txt.expandtabs()
# string.expandtabs(tabsize:optional(8))
# txt = "H\te\tl\tl\to"

txt.find()
# string.find(value, start:optional, end:optional)
# x = txt.find("e")

txt.format()
# string.format(value1, value2...)
# txt1 = "My name is {fname}, I'm {age}".format(fname = "Ana", age = 36)
# txt2 = "My name is {0}, I'm {1}".format("Kourosh",36)
# txt3 = "My name is {}, I'm {}".format("Mahtab",36)

# Formatting Types
txt = "The universe is {:,} years old."
print(txt.format(13800000000))  # // 13,800,000,000
txt = "The universe is {:_} years old."
print(txt.format(13800000000))  # // 13_800_000_000
txt = "We have {:E} chickens."
print(txt.format(5))  # // 5.000000E+00
txt = "The price is {:.2f} dollars."
print(txt.format(45))  # // 45.00
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))  # // +7
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))  # // 101
txt = "We have {:d} chickens."
print(txt.format(0b101))  # // 5

txt.format_map()
txt.index()
# string.index(value, start, end)
# [*] If the value is not found, the find() method returns -1, but the index() method will raise an exception:
txt = "Hello, welcome to my world."
x = txt.index("welcome")  # // 7
print(txt.find("q"))  # // -1
print(txt.index("q"))  # // error

txt.isalnum()
# string.isalnum():bool

txt.isalpha()
# string.isalpha():bool

txt.isdecimal()
# string.isdecimal():bool
# a = "\u0030" #unicode for 0
# b = "\u0047" #unicode for G
# print(a.isdecimal())
# print(b.isdecimal())

txt.isdigit()
# string.isdigit():bool
# a = "\u0030" #unicode for 0
# b = "\u00B2" #unicode for ²
# print(a.isdigit())
# print(b.isdigit())

txt.isidentifier()
# string.isidentifier():bool

txt.islower()
# string.islower():bool

txt.isnumeric()
# string.isnumeric():bool

txt.isprintable()
# string.isprintable():bool txt = "Hello!\nAre you #1?" \\ false "\n"

txt.isspace()
# string.isspace():bool

txt.istitle()
# Check if each word start with an upper case letter:

txt.isupper()

txt.join()
# string.join(iterable)
# Note: When using a dictionary as an iterable, the returned values are the keys, not the values.
# myTuple = {"John", "Peter", "Vicky"}
# x = "#".join(myTuple)
# print(x)  # // John#Vicky#Peter

txt.ljust()
# string.ljust(length, character)
# txt = "banana"
# x = txt.ljust(20, "O")
# print(x)

txt.lower()
# string.lower()

txt.lstrip()
# string.lstrip(characters)
# txt = ",,,,,ssaaww.....banana"
# x = txt.lstrip(",.asw")
# print(x)

txt.maketrans()

txt.partition()
# Note: This method search for the first occurrence of the specified string.
# txt = "I could eat bananas all day"
# x = txt.partition("bananas")
# print(x) #('I could eat ', 'bananas', ' all day')

txt.replace()
# txt = "one one was a race horse, two two was one too."
# x = txt.replace("one", "three", 2)
# print(x)

txt.rfind()

txt.rindex()
txt.rjust()
txt.rpartition()
txt.rsplit()
txt.rstrip()
txt.split()
txt.splitlines()
txt.startswith()
txt.strip()
txt.swapcase()
txt.title()
txt.translate()
txt.upper()
txt.zfill()

# [2] example

txt.casefold()
txt = 'ß'
# [!] txt.casefold() == txt.lower()  # // ???

txt.txtcenter(20)
