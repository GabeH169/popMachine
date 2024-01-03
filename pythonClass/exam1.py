itemsPrice = float(input("Item price: $"))
finalPrice = 0

if itemsPrice >= 500:
    tax = itemsPrice * .20
    finalPrice = itemsPrice - tax
elif itemsPrice >= 200 and itemsPrice < 500:
    tax = itemsPrice * .10
    finalPrice = itemsPrice - tax
else :
    finalPrice += itemsPrice

print(f"Final Price: ${finalPrice:,.2f}")