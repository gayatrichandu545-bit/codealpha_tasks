# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 320,
    "AMZN": 3500
}

portfolio = {}
total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Enter stock names (like AAPL, TSLA) and quantities.")
print("Type 'done' when finished.\n")

# Taking user input
while True:
    stock_name = input("Enter stock name (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("❌ Stock not found in price list. Try again.\n")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    except ValueError:
        print("❌ Please enter a valid number for quantity.\n")

# Display and calculate
output_lines = []
print("\n📊 Investment Summary:")
output_lines.append("📊 Investment Summary:\n")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    line = f"{stock}: {qty} shares × ${price} = ${investment}"
    print(line)
    output_lines.append(line)

print(f"\n💰 Total Investment: ${total_investment}")
output_lines.append(f"\n💰 Total Investment: ${total_investment}")

# Save to file (optional)
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        for line in output_lines:
            file.write(line + "\n")
    print("✅ Portfolio summary saved to 'portfolio_summary.txt'.")
