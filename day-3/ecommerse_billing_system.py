TAX_RATE = 18
SHIPPING_CHARGE = 100

print("===== ONLINE SHOPPING BILL =====")

customer_name = input("Enter customer name: ")
customer_id = input("Enter customer ID: ")

# Product details
product1_name = input("Enter product 1 name: ")
product1_price = float(input("Enter product 1 price: "))
product1_quantity = int(input("Enter product 1 quantity: "))

product2_name = input("Enter product 2 name: ")
product2_price = float(input("Enter product 2 price: "))
product2_quantity = int(input("Enter product 2 quantity: "))

product3_name = input("Enter product 3 name: ")
product3_price = float(input("Enter product 3 price: "))
product3_quantity = int(input("Enter product 3 quantity: "))

discount_percentage = float(input("Enter discount percentage: "))

# Calculate bill
product1_total = product1_price * product1_quantity
product2_total = product2_price * product2_quantity
product3_total = product3_price * product3_quantity

subtotal = product1_total + product2_total + product3_total

discount = subtotal * discount_percentage / 100

amount_after_discount = subtotal - discount

tax = amount_after_discount * TAX_RATE / 100

final_amount = amount_after_discount + tax + SHIPPING_CHARGE

# Some checks
has_discount = discount_percentage > 0
large_order = final_amount >= 50000

product1_name = product1_name.lower()
has_laptop = "laptop" in product1_name

# Final bill
print("\n===== FINAL BILL =====")

print("Customer:", customer_name)
print("Customer ID:", customer_id)

print("\nProduct 1:", product1_name)
print("Price:", product1_price)
print("Quantity:", product1_quantity)
print("Total:", product1_total)

print("\nProduct 2:", product2_name)
print("Price:", product2_price)
print("Quantity:", product2_quantity)
print("Total:", product2_total)

print("\nProduct 3:", product3_name)
print("Price:", product3_price)
print("Quantity:", product3_quantity)
print("Total:", product3_total)

print("\nSubtotal:", subtotal)
print("Discount:", discount)
print("Tax:", tax)
print("Shipping:", SHIPPING_CHARGE)
print("Final Amount:", final_amount)

print("\n===== ORDER DETAILS =====")
print("Has discount:", has_discount)
print("Large order:", large_order)
print("Contains laptop:", has_laptop)

print("\nData Types:")
print(type(customer_name))
print(type(product1_price))
print(type(product1_quantity))
print(type(final_amount))