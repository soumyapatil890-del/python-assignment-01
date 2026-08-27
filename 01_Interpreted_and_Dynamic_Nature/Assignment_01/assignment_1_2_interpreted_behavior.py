# Problem Name: Interpreted Behavior

# Statement:
# Write a script where line 1 and line 2 execute successfully,
# but line 3 contains a deliberate NameError by referencing
# an undefined variable.
#
# Run the script and observe the console output.
# Explain why lines 1 and 2 execute before the program crashes.


# Solution:

print("Line 1 executed successfully.")
print("Line 2 executed successfully.")

# Deliberate NameError:
print(undefined_variable)


# answer:
# The first two print statements execute successfully because
# Python executes the program during runtime and reaches them
# before encountering the error.
#
# When Python reaches the third statement, it tries to access
# undefined_variable, which has not been defined.
#
# Therefore, Python raises a NameError and stops executing the
# remaining statements.