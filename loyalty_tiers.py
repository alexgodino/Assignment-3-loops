def get_customer_data():
    """Collect customer total purchase amounts from user; return dict.
    If no input is provided, return sample data."""
    print("Customer Loyalty Tiers")
    print("=" * 40)
    customers = {}

    while True:
        name = input("Enter customer name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        if not name:
            print("Please enter a valid name.")
            continue
        try:
            amount = float(input(f"Total purchases for {name}: $"))
            if amount < 0:
                print("Amount cannot be negative.")
                continue
            customers[name] = amount
        except ValueError:
            print("Invalid amount; please enter a number.")

    if not customers:
        # sample data
        customers = {
            "Alice": 5500,
            "Bob": 3200,
            "Carol": 8700,
            "David": 750,
            "Eve": 4500,
            "Frank": 2100,
        }
        print("No input detected — using sample data.\n")

    return customers


def assign_tiers(customers):
    """Return a dict mapping customer -> tier based on purchase amount."""
    def tier_for(amount):
        if amount >= 5000:
            return 'Gold'
        if amount >= 1000:
            return 'Silver'
        return 'Bronze'

    return {name: {'amount': amt, 'tier': tier_for(amt)} for name, amt in customers.items()}


def count_tiers(customer_tiers):
    """Count how many customers are in each tier."""
    counts = {'Bronze': 0, 'Silver': 0, 'Gold': 0}
    for data in customer_tiers.values():
        counts[data['tier']] += 1
    return counts


def display_summary(customer_tiers):
    """Print a summary of counts per tier."""
    total_customers = len(customer_tiers)
    counts = count_tiers(customer_tiers)

    print("\nLoyalty Tier Summary")
    print("=" * 40)
    print(f"Total customers: {total_customers}\n")
    print(f"{'Tier':<10} {'Count':<6} {'%':<6}")
    print('-' * 24)
    for tier in ['Bronze', 'Silver', 'Gold']:
        count = counts[tier]
        pct = (count / total_customers * 100) if total_customers else 0
        print(f"{tier:<10} {count:<6} {pct:5.1f}%")
    print()


def main():
    customers = get_customer_data()
    customer_tiers = assign_tiers(customers)
    display_summary(customer_tiers)


if __name__ == '__main__':
    main()
