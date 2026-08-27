# Problem Name: Login Attempts

# Statement:
# Allow a maximum of 3 login attempts.
# Correct password: admin123
#
# If entered correctly:
# Login Successful
#
# Otherwise:
# Try Again
#
# If all attempts fail:
# Account Locked
#
# Use a while loop.


# Solution:

correct_password = "admin123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    attempts += 1

    if password == correct_password:
        print("Login Successful")
        break
    else:
        if attempts < max_attempts:
            print("Try Again")

if attempts == max_attempts and password != correct_password:
    print("Account Locked")


# answer:
# The while loop allows the user a maximum of three login attempts.
# The entered password is compared with the correct password.
# If the password matches, Login Successful is printed and the loop
# stops using break.
# If the password is incorrect, Try Again is displayed while attempts
# remain.
# After three incorrect attempts, Account Locked is displayed.