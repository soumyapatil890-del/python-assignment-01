# Assignment 1.3 - Strongly Typed Behavior

age = 20

# Original code - produces TypeError
# message = "I am " + age + " years old."
# print(message)


# Method 1: Explicit type casting
message_casting = "I am " + str(age) + " years old."

print("Using type casting:")
print(message_casting)


# Method 2: f-string
message_fstring = f"I am {age} years old."

print("\nUsing f-string:")
print(message_fstring)
