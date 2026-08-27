# Problem Name: Modifying Scope with global and nonlocal

# Statement:
#
# Scenario A - global:
# Write a function increment_counter() that modifies a global
# variable counter = 0.
# Each call should increase counter by 1.
# Demonstrate the output over 3 function calls.
#
# Scenario B - nonlocal:
# Write a nested function structure:
#
# Outer function:
# bank_account(initial_balance)
#
# It should contain a local variable balance.
#
# Inner function:
# make_withdrawal(amount)
#
# It should subtract amount from balance.
# Use the nonlocal keyword so the inner function can update
# the balance in the enclosing function scope.


# Solution:


# Scenario A: global

counter = 0


def increment_counter():
    global counter
    counter += 1


increment_counter()
print("Counter after call 1:", counter)

increment_counter()
print("Counter after call 2:", counter)

increment_counter()
print("Counter after call 3:", counter)


# Scenario B: nonlocal

def bank_account(initial_balance):

    balance = initial_balance

    def make_withdrawal(amount):
        nonlocal balance
        balance -= amount
        return balance

    return make_withdrawal


account = bank_account(1000)

print("Balance after withdrawal 1:", account(200))
print("Balance after withdrawal 2:", account(300))
print("Balance after withdrawal 3:", account(100))


# answer:
#
# Scenario A:
#
# The variable counter is defined in the global scope.
# Normally, assigning to counter inside a function would create
# a local variable.
#
# The global keyword tells Python that the function should modify
# the existing global counter instead of creating a new local one.
#
# Therefore the three function calls produce:
#
# Counter after call 1: 1
# Counter after call 2: 2
# Counter after call 3: 3
#
#
# Scenario B:
#
# The variable balance belongs to the enclosing bank_account()
# function.
#
# The nested make_withdrawal() function needs to modify that
# enclosing variable.
#
# The nonlocal keyword tells Python to use the balance variable
# from the enclosing function scope.
#
# Starting balance = 1000
#
# Withdrawal 1:
# 1000 - 200 = 800
#
# Withdrawal 2:
# 800 - 300 = 500
#
# Withdrawal 3:
# 500 - 100 = 400
#
# Therefore the final output is:
#
# Balance after withdrawal 1: 800
# Balance after withdrawal 2: 500
# Balance after withdrawal 3: 400