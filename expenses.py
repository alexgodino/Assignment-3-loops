def get_categorized_expenses():
    """Get expense data from user or use sample data."""
    print("Expense Report Categorizer")
    print("=" * 50)
    print("Categories: Travel, Meals, Supplies\n")
    
    expenses = {
        "Travel": [],
        "Meals": [],
        "Supplies": []
    }
    
    print("Enter expenses by category (enter 0 to finish a category).\n")
    
    for category in expenses.keys():
        print(f"Enter {category} expenses:")
        while True:
            try:
                amount = float(input(f"  {category} expense: $"))
                if amount < 0:
                    print("  Amount cannot be negative.")
                    continue
                if amount == 0:
                    break
                expenses[category].append(amount)
            except ValueError:
                print("  Invalid input. Please enter a valid number.")
        if expenses[category]:
            print(f"  Total {category}: ${sum(expenses[category]):.2f}\n")
        else:
            print(f"  No {category} expenses entered.\n")
    
    # Check if any data was entered
    if all(len(expenses[cat]) == 0 for cat in expenses):
        print("No expenses entered. Using sample data.\n")
        expenses = {
            "Travel": [500, 200],
            "Meals": [40, 60, 30],
            "Supplies": [100]
        }
    
    return expenses


def calculate_category_total(expenses_list):
    """Calculate total for a single category."""
    return sum(expenses_list)


def calculate_grand_total(expenses):
    """Calculate the grand total across all categories."""
    grand_total = 0
    for category in expenses:
        grand_total += calculate_category_total(expenses[category])
    return grand_total


def calculate_percentage(category_total, grand_total):
    """Calculate percentage of category total to grand total."""
    if grand_total == 0:
        return 0
    return (category_total / grand_total) * 100


def count_expenses(expenses_list):
    """Count number of expenses in a list."""
    return len(expenses_list)


def display_expense_summary(expenses):
    """Display a formatted expense summary report."""
    if not expenses or all(len(expenses[cat]) == 0 for cat in expenses):
        print("No expenses to report.")
        return
    
    grand_total = calculate_grand_total(expenses)
    
    print("\n" + "=" * 50)
    print("EXPENSE SUMMARY REPORT")
    print("=" * 50)
    print(f"{'Category':<15} {'Count':<8} {'Total':<15} {'% of Total':<12}")
    print("-" * 50)
    
    # Nested loop through categories and their expenses
    for category in expenses:
        expenses_list = expenses[category]
        if len(expenses_list) > 0:
            category_total = calculate_category_total(expenses_list)
            count = count_expenses(expenses_list)
            percentage = calculate_percentage(category_total, grand_total)
            print(f"{category:<15} {count:<8} ${category_total:<14.2f} {percentage:<11.1f}%")
    
    print("-" * 50)
    print(f"{'GRAND TOTAL':<15} {'':<8} ${grand_total:<14.2f} {'100.0%':<11}")
    print("=" * 50 + "\n")


def print_detailed_expenses(expenses):
    """Print detailed breakdown of each expense."""
    print("\nDETAILED EXPENSE BREAKDOWN")
    print("-" * 50)
    
    for category in expenses:
        if len(expenses[category]) > 0:
            print(f"\n{category}:")
            for i, expense in enumerate(expenses[category], 1):
                print(f"  {i}. ${expense:.2f}")


def main():
    """Main function to run the expense categorizer."""
    expenses = get_categorized_expenses()
    display_expense_summary(expenses)
    print_detailed_expenses(expenses)


if __name__ == "__main__":
    main()
