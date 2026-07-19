# Stock Portfolio Tracker

# Hardcoded stock prices (in Indian Rupees)
stock_prices = {
    "AAPL": 15000,
    "TSLA": 21000,
    "GOOGL": 12500,
    "MSFT": 27000,
    "AMZN": 11600
}

total_investment = 0

# Open file to save the portfolio
file = open("portfolio.txt", "w", encoding="utf-8")

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available Stocks:")
for stock, price in stock_prices.items():
    print(stock, "- ₹", price)

n = int(input("\nEnter the number of different stocks: "))

file.write("Stock Portfolio Report\n")
file.write("----------------------\n")

for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Investment in", stock_name, "= ₹", investment)

        file.write(f"{stock_name} - Quantity: {quantity}, Investment: ₹{investment}\n")
    else:
        print("Stock not available!")

print("\nTotal Investment Value = ₹", total_investment)

file.write("\nTotal Investment Value = ₹" + str(total_investment))
file.close()

print("Portfolio saved successfully in 'portfolio.txt'")
