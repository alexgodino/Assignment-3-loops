def get_prices():
    """Get item prices from the customer until 0 is entered."""
    prices = []
    while True:
        try:
            price = float(input("Enter item price (or 0 to finish): $"))
            if price < 0:
                print("Price cannot be negative. Please try again.")
                continue
            if price == 0:
                break
            prices.append(price)
            print(f"Item added. Running total: ${sum(prices):.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return prices


def calculate_total(prices):
    """Calculate the total purchase amount."""
    return sum(prices)


def calculate_average(prices):
    """Calculate the average item cost."""
    if len(prices) == 0:
        return 0
    return sum(prices) / len(prices)


def get_item_count(prices):
    """Get the number of items purchased."""
    return len(prices)


def display_receipt(prices):
    """Display the checkout receipt with all purchase details."""
    total = calculate_total(prices)
    average = calculate_average(prices)
    num_items = get_item_count(prices)
    
    print("\n" + "=" * 40)
    print("CHECKOUT RECEIPT")
    print("=" * 40)
    print(f"Number of items bought: {num_items}")
    print(f"Total purchase amount: ${total:.2f}")
    if num_items > 0:
        print(f"Average item cost: ${average:.2f}")
    print("=" * 40 + "\n")


def main():
    """Main function to run the checkout simulation."""
    print("Welcome to the Retail Checkout System!")
    print("Enter prices of items you are buying.")
    print("Enter 0 to finish.\n")
    
    prices = get_prices()
    
    if prices:
        display_receipt(prices)
    else:
        print("No items were purchased.")


if __name__ == "__main__":
    main()
