import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "MSFT": 320,
    "AMZN": 150
}

portfolio = {}
total = 0

print("====== STOCK PORTFOLIO TRACKER ======")

while True:
    stock = input("Enter Stock Name (or 'done'): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter Quantity: "))
    portfolio[stock] = quantity

print("\nPortfolio Summary")
print("--------------------------")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total += value
    print(f"{stock}: {quantity} x ${stock_prices[stock]} = ${value}")

print("--------------------------")
print("Total Investment Value = $", total)

# Save to CSV
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Stock", "Quantity", "Price", "Value"])

    for stock, quantity in portfolio.items():
        writer.writerow([
            stock,
            quantity,
            stock_prices[stock],
            stock_prices[stock] * quantity
        ])

    writer.writerow([])
    writer.writerow(["Total", "", "", total])

print("\nPortfolio saved as portfolio.csv")