# [1] Python Collections (Arrays)
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

list = ["apple", "banana", "cherry"]
print(list)
print(list[1])
print(list[-1])
print(list[2:5])
print(list[:4])
print(list[2:])
print(list[-4:-1])
# [*] Note: The search will start at index 2 (included) and end at index 5 (not included).#
# [*] Remember that the first item has index 0.

# Change Item Value
list[1] = "blackcurrant"

# [2] Loop Through a List
for x in list:
    print(x)

# Check if Item Exists
if "apple" in list:
    print("Yes, 'apple' is in the fruits list")

# List Length
print(len(list))

# Add Items
list.append("orange")

list.insert(1, "orange")

# Remove Item
list.remove("banana")  # specified item

list.pop()  # last
list.pop(0)  # index
del list[0]
del list  # error
list.clear()  # all

# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1,
# and changes made in list1 will automatically also be made in list2.
new_list = list.copy()
new_list = list(list)  # same above # todo error ?

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2

# another ways
for x in list2:
    list1.append(x)

list1.extend(list2)
print(list1)

# The list() Constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)