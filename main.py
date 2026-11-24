
from discount import calculate_discount

print("===== SMART DISCOUNT CALCULATOR =====")

price = float(input("Enter product price: ₹"))

print("\n1. Percentage Discount")
print("2. Fixed Discount")

choice = input("Choose discount type: ")

if choice == "1":
    discount_type = "percentage"
    value = float(input("Enter discount percentage: "))

elif choice == "2":
    discount_type = "fixed"
    value = float(input("Enter discount amount: ₹"))

else:
    print("Invalid choice")
    exit()

try:
    result = calculate_discount(price, discount_type, value)

    print("\n===== DISCOUNT SUMMARY =====")
    print(f"Original Price : ₹{result['original_price']}")
    print(f"You Save       : ₹{result['discount']}")
    print(f"Final Price    : ₹{result['final_price']}")

except ValueError as error:
    print("Error:", error)
