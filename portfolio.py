import random


def get_portfolio_data():
    """Get portfolio data from user or use sample data."""
    print("Stock Portfolio Tracker")
    print("=" * 60)
    print("Build your investment portfolio.\n")
    
    portfolio = {}
    
    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").strip().upper()
        if symbol == 'DONE':
            break
        if not symbol:
            print("Please enter a valid symbol.\n")
            continue
        
        try:
            shares = float(input(f"Number of {symbol} shares: "))
            if shares < 0:
                print("Shares cannot be negative.\n")
                continue
            
            price = float(input(f"{symbol} current price per share: $"))
            if price < 0:
                print("Price cannot be negative.\n")
                continue
            
            portfolio[symbol] = {
                "shares": shares,
                "price": price
            }
            value = shares * price
            print(f"{symbol} added: {shares} shares @ ${price:.2f} = ${value:.2f}\n")
        except ValueError:
            print("Invalid input. Please enter valid numbers.\n")
    
    # Use sample data if none entered
    if not portfolio:
        print("No portfolio data entered. Using sample data.\n")
        portfolio = {
            "AAPL": {"shares": 10, "price": 170},
            "TSLA": {"shares": 4, "price": 250},
            "AMZN": {"shares": 2, "price": 130},
            "GOOGL": {"shares": 5, "price": 140},
            "MSFT": {"shares": 3, "price": 380}
        }
    
    return portfolio


def calculate_stock_value(shares, price):
    """Calculate total value for a single stock."""
    return shares * price


def calculate_portfolio_value(portfolio):
    """Calculate total portfolio value using nested loops."""
    total_value = 0
    for symbol in portfolio:
        stock_data = portfolio[symbol]
        shares = stock_data["shares"]
        price = stock_data["price"]
        total_value += calculate_stock_value(shares, price)
    return total_value


def get_stock_details(portfolio, symbol):
    """Get details for a specific stock."""
    if symbol in portfolio:
        return portfolio[symbol]
    return None


def simulate_price_change(current_price, change_percent=5):
    """Simulate random daily price change (±percentage)."""
    change_range = current_price * (change_percent / 100)
    price_change = random.uniform(-change_range, change_range)
    new_price = max(current_price + price_change, 0.01)  # Price cannot go below 0.01
    return new_price


def update_portfolio_prices(portfolio, change_percent=5):
    """Update all stock prices with random daily changes."""
    for symbol in portfolio:
        old_price = portfolio[symbol]["price"]
        new_price = simulate_price_change(old_price, change_percent)
        portfolio[symbol]["price"] = new_price


def calculate_price_change(old_price, new_price):
    """Calculate price change amount and percentage."""
    change_amount = new_price - old_price
    change_percent = (change_amount / old_price) * 100 if old_price != 0 else 0
    return change_amount, change_percent


def display_portfolio_summary(portfolio, day=None):
    """Display formatted portfolio summary."""
    if not portfolio:
        print("Portfolio is empty.")
        return
    
    total_value = calculate_portfolio_value(portfolio)
    
    if day is not None:
        print(f"\n{'=' * 80}")
        print(f"PORTFOLIO SUMMARY - DAY {day}")
        print(f"{'=' * 80}")
    else:
        print(f"\n{'=' * 80}")
        print("PORTFOLIO SUMMARY")
        print(f"{'=' * 80}")
    
    print(f"{'Symbol':<10} {'Shares':<12} {'Price':<15} {'Value':<15} {'Total Value':<15}")
    print("-" * 80)
    
    for symbol in sorted(portfolio.keys()):
        stock_data = portfolio[symbol]
        shares = stock_data["shares"]
        price = stock_data["price"]
        value = calculate_stock_value(shares, price)
        print(f"{symbol:<10} {shares:<12.2f} ${price:<14.2f} ${value:<14.2f}")
    
    print("-" * 80)
    print(f"{'TOTAL PORTFOLIO VALUE':<10} {'':<12} {'':<15} {'':<15} ${total_value:<14.2f}")
    print(f"{'=' * 80}\n")


def display_detailed_portfolio(portfolio):
    """Display detailed portfolio with calculated values."""
    if not portfolio:
        print("Portfolio is empty.")
        return
    
    total_value = calculate_portfolio_value(portfolio)
    
    print("\nDETAILED PORTFOLIO BREAKDOWN")
    print("-" * 80)
    
    for symbol in sorted(portfolio.keys()):
        stock_data = portfolio[symbol]
        shares = stock_data["shares"]
        price = stock_data["price"]
        value = calculate_stock_value(shares, price)
        percentage = (value / total_value) * 100
        print(f"{symbol}: {shares} shares @ ${price:.2f} = ${value:.2f} ({percentage:.1f}% of portfolio)")


def simulate_week(portfolio):
    """Simulate a week of trading with daily price changes."""
    print("\n" + "=" * 80)
    print("WEEKLY SIMULATION - RANDOM PRICE CHANGES (±5% daily)")
    print("=" * 80)
    
    # Store original prices
    original_prices = {}
    for symbol in portfolio:
        original_prices[symbol] = portfolio[symbol]["price"]
    
    # Simulate each day
    for day in range(1, 8):
        print(f"\n--- DAY {day} ---")
        update_portfolio_prices(portfolio, change_percent=5)
        
        # Show price changes
        for symbol in sorted(portfolio.keys()):
            old_price = original_prices[symbol] if day == 1 else portfolio[symbol]["price"]
            new_price = portfolio[symbol]["price"]
            
            # For days after day 1, calculate change from previous
            if day > 1:
                old_price = portfolio[symbol]["price"]
                new_price = simulate_price_change(old_price, change_percent=5)
                portfolio[symbol]["price"] = new_price
            
            change_amount, change_percent = calculate_price_change(original_prices[symbol], new_price)
            change_indicator = "↑" if change_percent > 0 else "↓" if change_percent < 0 else "→"
            print(f"{symbol}: ${new_price:.2f} ({change_indicator} {change_percent:+.2f}%)")
        
        portfolio_value = calculate_portfolio_value(portfolio)
        print(f"Portfolio Value: ${portfolio_value:.2f}")
    
    print("\n" + "=" * 80)


def main():
    """Main function to run the portfolio tracker."""
    portfolio = get_portfolio_data()
    
    display_portfolio_summary(portfolio)
    display_detailed_portfolio(portfolio)
    
    # Ask if user wants to simulate a week
    while True:
        choice = input("Simulate a week of trading? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            simulate_week(portfolio)
            break
        elif choice in ['no', 'n']:
            print("\nThank you for using the Portfolio Tracker!")
            break
        else:
            print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
