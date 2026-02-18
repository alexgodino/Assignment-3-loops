def get_sales_data():
    """Get sales data from user or use sample data."""
    print("Sales Commission Calculator")
    print("=" * 50)
    print("Enter employee sales data.\n")
    
    sales = {}
    
    while True:
        name = input("Enter employee name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        if not name:
            print("Please enter a valid name.\n")
            continue
        
        try:
            amount = float(input(f"Enter {name}'s sales amount: $"))
            if amount < 0:
                print("Sales amount cannot be negative.\n")
                continue
            sales[name] = amount
            print(f"{name}'s sales recorded: ${amount:.2f}\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
    
    # Use sample data if none entered
    if not sales:
        print("No sales data entered. Using sample data.\n")
        sales = {
            "Alice": 5000,
            "Bob": 7000,
            "Carol": 3000,
            "David": 8500,
            "Eve": 4200
        }
    
    return sales


def calculate_commission(sales_amount, commission_rate=0.10):
    """Calculate commission for a single employee."""
    return sales_amount * commission_rate


def calculate_all_commissions(sales):
    """Calculate commissions for all employees."""
    commissions = {}
    for employee, sales_amount in sales.items():
        commissions[employee] = calculate_commission(sales_amount)
    return commissions


def rank_employees(commissions):
    """Rank employees by commission earned (highest to lowest)."""
    return sorted(commissions.items(), key=lambda x: x[1], reverse=True)


def get_total_commissions(commissions):
    """Calculate total commissions paid out."""
    return sum(commissions.values())


def get_average_commission(commissions):
    """Calculate average commission per employee."""
    if len(commissions) == 0:
        return 0
    return get_total_commissions(commissions) / len(commissions)


def display_leaderboard(sales, commissions):
    """Display a formatted leaderboard of employees ranked by commission."""
    if not sales:
        print("No sales data to display.")
        return
    
    ranked = rank_employees(commissions)
    total_commissions = get_total_commissions(commissions)
    avg_commission = get_average_commission(commissions)
    
    print("\n" + "=" * 60)
    print("SALES COMMISSION LEADERBOARD")
    print("=" * 60)
    print(f"{'Rank':<6} {'Employee':<15} {'Sales':<15} {'Commission':<15}")
    print("-" * 60)
    
    for rank, (employee, commission) in enumerate(ranked, 1):
        employee_sales = sales[employee]
        print(f"{rank:<6} {employee:<15} ${employee_sales:<14.2f} ${commission:<14.2f}")
    
    print("-" * 60)
    print(f"{'':6} {'Total Commissions':<15} {'':<15} ${total_commissions:<14.2f}")
    print(f"{'':6} {'Average Commission':<15} {'':<15} ${avg_commission:<14.2f}")
    print("=" * 60 + "\n")


def main():
    """Main function to run the commission calculator."""
    sales = get_sales_data()
    commissions = calculate_all_commissions(sales)
    display_leaderboard(sales, commissions)


if __name__ == "__main__":
    main()
