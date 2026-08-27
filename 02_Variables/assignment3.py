# Problem Name: Grocery Bill

# Statement:
# Store:
# Shop Name
# Item 1 Price
# Item 2 Price
# Item 3 Price
#
# Create variables for:
# Total
# GST (18%)
# Final Amount
#
# Print a formatted bill.


# Solution:

shop_name = "ABC Grocery Store"

item1_price = 100
item2_price = 250
item3_price = 150

total = item1_price + item2_price + item3_price

gst = total * 0.18

final_amount = total + gst


print("=" * 40)
print("             GROCERY BILL")
print("=" * 40)
print(f"Shop Name    : {shop_name}")
print(f"Item 1 Price : ₹{item1_price:.2f}")
print(f"Item 2 Price : ₹{item2_price:.2f}")
print(f"Item 3 Price : ₹{item3_price:.2f}")
print("-" * 40)
print(f"Total        : ₹{total:.2f}")
print(f"GST (18%)    : ₹{gst:.2f}")
print(f"Final Amount : ₹{final_amount:.2f}")
print("=" * 40)


# answer:
# The three item prices are stored in separate variables.
# Total is calculated by adding the three item prices.
# GST is calculated as 18% of the total.
# Final Amount is calculated by adding GST to the total.
# The result is displayed as a formatted grocery bill.