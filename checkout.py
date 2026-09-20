def calculate_total(price, quantity, tax_rate=0.06):
    subtotal = price * quantity
    total = subtotal * (1 + tax_rate)
    return total

print(calculate_total(10, 3))