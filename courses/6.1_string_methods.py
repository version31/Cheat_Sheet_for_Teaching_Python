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
txt.isalpha()
txt.isdecimal()
txt.isdigit()
txt.isidentifier()
txt.islower()
txt.isnumeric()
txt.isprintable()
txt.isspace()
txt.istitle()
txt.isupper()
txt.join()
txt.ljust()
txt.lower()
txt.lstrip()
txt.maketrans()
txt.partition()
txt.replace()
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
