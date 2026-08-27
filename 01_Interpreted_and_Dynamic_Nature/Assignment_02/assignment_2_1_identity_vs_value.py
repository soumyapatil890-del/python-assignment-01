# Problem Name: Identity vs. Value

# Statement:
# Analyze mutable objects using == and is.
# Print object identities using id().
# Demonstrate shared references and mutability.
# Explore small integer caching using 256 and 257.
#
# Questions:
# 1. Why does list1 == list2 evaluate to True while
#    list1 is list2 evaluates to False?
# 2. What happens to list3 if list1.append(4) is executed? Why?
# 3. Why does a is b return True for 256, but x is y might
#    return False for 257 in a standard Python REPL?
#    Explain using small integer caching.


# Solution:


# Part A: Mutables

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2:", list1 == list2)
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)


# Part B: Memory IDs

print("ID of list1:", id(list1))
print("ID of list2:", id(list2))
print("ID of list3:", id(list3))


# Part C: Small Integer Caching

a = 256
b = 256

print("a is b (256):", a is b)

x = 257
y = 257

print("x is y (257):", x is y)


# Part D: Shared Reference and Mutability

list1.append(4)

print("After list1.append(4):")
print("list1:", list1)
print("list3:", list3)


# answer:
#
# 1. list1 == list2 is True because == compares the values
#    stored in the two lists. Both lists contain [1, 2, 3].
#
#    list1 is list2 is False because is checks whether both
#    variables refer to the exact same object in memory.
#    list1 and list2 are two different list objects.
#
# 2. list3 refers to the same list object as list1 because:
#
#       list3 = list1
#
#    Therefore, when list1.append(4) is executed, the shared list
#    object is modified and list3 also shows [1, 2, 3, 4].
#
# 3. Python commonly caches small integer objects, including
#    integers in the range containing 256. Therefore, a and b
#    may refer to the same integer object, making:
#
#       a is b
#
#    True.
#
#    For 257, object identity is not guaranteed in the same way.
#    Therefore x is y may be False in a standard Python REPL.
#
#    The exact identity result can depend on the execution
#    environment, so `is` should not be used to compare numeric
#    values.
#
#    Use == for value comparison and is for object identity.