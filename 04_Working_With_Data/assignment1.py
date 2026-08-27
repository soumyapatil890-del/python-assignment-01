# Problem Name: Electricity Bill

# Statement:
# Store:
# Previous Reading
# Current Reading
# Cost per Unit
#
# Calculate:
# Units Consumed
# Total Bill
#
# Print the bill.


# Solution:

previous_reading = 1200
current_reading = 1450
cost_per_unit = 8

units_consumed = current_reading - previous_reading
total_bill = units_consumed * cost_per_unit


print("=" * 40)
print("          ELECTRICITY BILL")
print("=" * 40)
print(f"Previous Reading : {previous_reading}")
print(f"Current Reading  : {current_reading}")
print(f"Cost per Unit    : ₹{cost_per_unit:.2f}")
print(f"Units Consumed   : {units_consumed}")
print(f"Total Bill       : ₹{total_bill:.2f}")
print("=" * 40)


# answer:
# Units Consumed = Current Reading - Previous Reading.
# Total Bill = Units Consumed × Cost per Unit.
# In this example:
# Units Consumed = 1450 - 1200 = 250 units.
# Total Bill = 250 × 8 = ₹2000.