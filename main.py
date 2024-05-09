items = []
prices = []
total = 0

while True:
    item = input("What item would you like to add to your shopping list? (Enter q to quit): ")
    if item.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {item}: £"))
        items.append(item)
        prices.append(price)

print("----- YOUR SHOPPING LIST -----")

for item in items:
    print(item, end=", ")

for price in prices:
    total += price

print()
print(f"Your total is £{total}")