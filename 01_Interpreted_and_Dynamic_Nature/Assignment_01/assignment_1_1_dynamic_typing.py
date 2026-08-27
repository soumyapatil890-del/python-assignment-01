# Problem Name: Dynamic Typing

# Statement:
# Create a variable named data.
# Assign an integer to it, then print its value and type using type().
# Reassign a list to data.
# Print its value and type again.


# Solution:

data = 100

print("Value:", data)
print("Type:", type(data))

data = [10, 20, 30]

print("Value:", data)
print("Type:", type(data))


# answer:
# Initially, data stores the integer value 100, so its type is int.
#
# Later, the same variable data is reassigned to the list
# [10, 20, 30], so its type becomes list.
#
# This demonstrates dynamic typing in Python because the type of
# a variable is determined at runtime and the same variable can
# refer to objects of different types during program execution.