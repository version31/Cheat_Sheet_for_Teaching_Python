# Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Most Values are True
bool("abc")
bool(123)
bool(-1)
bool(["apple", "cherry", "banana"])

# Some Values are False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# [*]
class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))


# Functions can Return a Boolean
def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

# many built-in functions that returns a boolean value
x = 200
print(isinstance(x, int))
