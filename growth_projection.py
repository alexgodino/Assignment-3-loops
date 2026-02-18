def get_growth_inputs():
    """Prompt user for initial revenue and annual growth rate.

    Returns a tuple (initial_revenue: float, growth_rate_percent: float, years: int).
    If the user provides invalid input or nothing, sample defaults are used.
    """
    print("Business Growth Projection")
    print("=" * 40)
    try:
        initial = input("Enter initial revenue (or press Enter for $100000): $").strip()
        if initial == "":
            initial_rev = 100000.0
        else:
            initial_rev = float(initial)
            if initial_rev < 0:
                print("Revenue cannot be negative. Using default $100000.")
                initial_rev = 100000.0

        rate = input("Enter annual growth rate percent (e.g., 5 for 5%) (default 5): ").strip()
        if rate == "":
            growth_rate = 5.0
        else:
            growth_rate = float(rate)

        years_in = input("Enter number of years to project (default 10): ").strip()
        if years_in == "":
            years = 10
        else:
            years = int(years_in)
            if years <= 0:
                print("Number of years must be positive. Using default 10.")
                years = 10

        return initial_rev, growth_rate, years
    except ValueError:
        print("Invalid input detected — using defaults: $100000, 5%, 10 years.")
        return 100000.0, 5.0, 10


def project_growth(initial_revenue, growth_rate_percent, years=10):
    """Project revenue year-by-year.

    Returns a list of dicts: [{'year': 0, 'revenue': initial}, {'year': 1, 'revenue': ...}, ...]
    Year 0 is the starting revenue; years 1..N show revenue after each year of growth.
    """
    results = []
    results.append({'year': 0, 'revenue': float(initial_revenue)})
    rate = growth_rate_percent / 100.0
    current = float(initial_revenue)
    for y in range(1, years + 1):
        current = current * (1 + rate)
        results.append({'year': y, 'revenue': current})
    return results


def display_projection(projection_list):
    """Print a neat table of year-by-year revenue projection."""
    if not projection_list:
        print("No projection data to display.")
        return

    print("\nRevenue Projection")
    print("=" * 40)
    print(f"{'Year':<6} {'Revenue':>20}")
    print('-' * 28)
    for entry in projection_list:
        year = entry['year']
        rev = entry['revenue']
        print(f"{year:<6} ${rev:>19,.2f}")
    print()


def main():
    initial, rate, years = get_growth_inputs()
    projection = project_growth(initial, rate, years)
    display_projection(projection)


if __name__ == '__main__':
    main()
