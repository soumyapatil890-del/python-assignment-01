# Problem Name: Strongly Typed Behavior

# Statement:
# Write the following snippet attempting to concatenate
# an integer and a string:
#
# age = 20
# message = "I am " + age + " years old."
#
# Tasks:
# 1. Identify the error raised by the original code.
# 2. Fix the error using explicit type casting.
# 3. Fix the error using an f-string.
# 4. Explain why this demonstrates strong typing.


# Solution:

age = 20

# Original code:
# message = "I am " + age + " years old."

print("Original Attempt:")

try:
    message = "I am " + age + " years old."
    print(message)
except TypeError as error:
    print("Error:", error)


# Fix 1: Explicit type casting using str()

message_casting = "I am " + str(age) + " years old."

print("\nFix 1 - Explicit Type Casting:")
print(message_casting)


# Fix 2: Using an f-string

message_fstring = f"I am {age} years old."

print("\nFix 2 - F-string:")
print(message_fstring)


# answer:
# The original code raises a TypeError because Python does not
# automatically convert the integer age into a string when
# performing string concatenation.
#
# The first solution explicitly converts age from int to str
# using str(age).
#
# The second solution uses an f-string, where Python formats
# the integer value as part of the string.
#
# This demonstrates strong typing because Python does not
# silently combine incompatible types such as str and int.
# The programmer must explicitly make the types compatible.