def calculate_total(price, quantity, tax_rate=0.06):
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

print(calculate_total(10, 3))