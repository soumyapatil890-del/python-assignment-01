# Problem Name: ATM Withdrawal

# Statement:
# Store:
# Account Balance
# Withdrawal Amount
#
# If balance is sufficient:
# Transaction Successful
#
# Otherwise:
# Insufficient Balance
#
# Print remaining balance if withdrawal succeeds.


# Solution:

account_balance = 5000
withdrawal_amount = 2000

if withdrawal_amount <= account_balance:
    remaining_balance = account_balance - withdrawal_amount
    print("Transaction Successful")
    print(f"Remaining Balance: ₹{remaining_balance:.2f}")
else:
    print("Insufficient Balance")


# answer:
# The program compares the withdrawal amount with the account balance.
# If the withdrawal amount is less than or equal to the balance,
# the transaction succeeds and the remaining balance is calculated.
# Otherwise, the program prints "Insufficient Balance".