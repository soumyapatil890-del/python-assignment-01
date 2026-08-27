# Problem Name: Product Discount

# Statement:
# Store:
# Product Price
# Discount Percentage
#
# Calculate:
# Discount Amount
# Final Price
#
# Round the final price to two decimals.


# Solution:

product_price = 2499
discount_percentage = 15

discount_amount = product_price * discount_percentage / 100
final_price = product_price - discount_amount
final_price = round(final_price, 2)


print("=" * 40)
print("         PRODUCT DISCOUNT")
print("=" * 40)
print(f"Product Price       : ₹{product_price:.2f}")
print(f"Discount Percentage : {discount_percentage}%")
print(f"Discount Amount     : ₹{discount_amount:.2f}")
print(f"Final Price         : ₹{final_price:.2f}")
print("=" * 40)


# answer:
# Discount Amount = Product Price × Discount Percentage / 100.
# Final Price = Product Price - Discount Amount.
# The final price is rounded to two decimal places using round().
#
# In this example:
# Discount Amount = 2499 × 15 / 100 = ₹374.85
# Final Price = 2499 - 374.85 = ₹2124.15