# Set
# Note: the set list is unordered, meaning: the items will appear in a random order.
thisset = {"apple", "banana", "cherry"}
print(thisset)  # // {'cherry', 'banana', 'apple'}

# Access Items
# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

print("banana" in thisset)  # // True

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.
