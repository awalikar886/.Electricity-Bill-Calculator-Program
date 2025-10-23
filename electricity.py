rate_per_unit = 5
units = int(input("Enter Units Consumed: "))

total_bill = units * rate_per_unit

print(f"Units Consumed: {units}")
print(f"Total Bill: ₹{total_bill:.0f}")

if total_bill > 1000:
    discount = total_bill * 0.10
    final_bill = total_bill - discount
    print(f"Discount Applied: ₹{discount:.0f}")
    print(f"Final Bill: ₹{final_bill:.0f}")
else:
    print("No discount applied.")
