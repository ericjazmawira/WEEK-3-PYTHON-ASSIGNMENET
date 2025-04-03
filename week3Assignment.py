def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

# user nput
price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount)

# Print the final price
if discount >= 20:
    print(f"Final price after discount: Ksh {final_price:.2f}")
else:
    print(f"No discount applied. Final price: Ksh {final_price:.2f}")
