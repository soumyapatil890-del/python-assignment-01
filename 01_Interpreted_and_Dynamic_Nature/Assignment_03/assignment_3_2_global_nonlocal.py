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