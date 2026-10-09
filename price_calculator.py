# Program: Item Total Price Calculator
# Purpose: Takes item price and quantity inputs, calculates the total, and formats the summary.

# Step 1: Prompt the user for input
price_input = input("Enter the price of one item ($): ")
quantity_input = input("Enter the quantity you want to buy: ")

# Step 2: Convert inputs from strings to numeric types
# float() allows decimal prices, int() ensures whole number quantities
price = float(price_input)
quantity = int(quantity_input)

# Step 3: Calculate the total cost
total_cost = price * quantity

# Step 4: Display a formatted summary using an f-string
# :.2f formats the price and total to two decimal places
print(f"\nSummary: {quantity} items at ${price:.2f} each = ${total_cost:.2f}")