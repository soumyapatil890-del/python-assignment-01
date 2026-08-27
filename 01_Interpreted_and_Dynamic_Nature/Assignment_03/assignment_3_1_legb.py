# Problem Name: LEGB Lookup Order in Action

# Statement:
# Analyze and run the following code.
#
# Demonstrate the LEGB rule:
# Local
# Enclosing
# Global
# Built-in
#
# Trace the output of the program.
# Then comment out x = "Local X" inside inner() and observe
# which value is printed.
# Then comment out x = "Enclosing X" inside outer() as well
# and observe which value is printed.
#
# Identify which part of LEGB is used at each step.


# Solution:


x = "Global X"


def outer():
    x = "Enclosing X"

    def inner():
        x = "Local X"
        print("Inner x:", x)

    inner()
    print("Outer x:", x)


outer()
print("Main x:", x)


# answer:
#
# Initial execution:
#
# Inner x: Local X
# Outer x: Enclosing X
# Main x: Global X
#
# The lookup for x inside inner() first checks the Local scope.
# Therefore, "Local X" is found first.
#
# If x = "Local X" inside inner() is commented out,
# Python searches the Enclosing scope and finds:
#
# x = "Enclosing X"
#
# Therefore Inner x becomes:
#
# Inner x: Enclosing X
#
# If x = "Enclosing X" inside outer() is also commented out,
# Python continues searching the Global scope and finds:
#
# x = "Global X"
#
# Therefore Inner x becomes:
#
# Inner x: Global X
#
# LEGB stands for:
#
# L - Local
# E - Enclosing
# G - Global
# B - Built-in
#
# Python searches these scopes in this order when resolving names.