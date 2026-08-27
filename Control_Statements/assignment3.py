# Problem Name: Even Numbers Printer

# Statement:
# Print all even numbers from 1 to 50 using a for loop.
# Also print how many even numbers were printed.


# Solution:

count = 0

for number in range(1, 51):
    if number % 2 == 0:
        print(number)
        count += 1

print(f"Total even numbers: {count}")


# answer:
# The for loop checks every number from 1 to 50.
# The modulo operator (%) is used to check whether a number is even.
# If number % 2 is 0, the number is even and it is printed.
# The count variable increases each time an even number is printed.
# There are 25 even numbers from 1 to 50.