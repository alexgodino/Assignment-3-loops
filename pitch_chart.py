def get_projection_values():
    """Collect initial revenue and growth rate, return list of year revenues (1..years)."""
    try:
        initial = float(input("Initial revenue (or press Enter for 100000): $") or 100000)
    except ValueError:
        print("Invalid input — using 100000.")
        initial = 100000.0

    try:
        rate = float(input("Annual growth rate percent (e.g., 5): ") or 5)
    except ValueError:
        print("Invalid input — using 5%.")
        rate = 5.0

    try:
        years = int(input("Years to project (default 10): ") or 10)
    except ValueError:
        print("Invalid input — using 10 years.")
        years = 10

    results = []
    factor = 1 + rate / 100.0
    current = float(initial)
    for y in range(1, years + 1):
        current = current * factor
        results.append((y, current))
    return results


def build_bar(value, max_value, max_width=50):
    """Build an ASCII bar for a single value scaled to max_width.

    Uses nested loops and character accumulation rather than direct string multiplication,
    to demonstrate nested loop usage.
    """
    if max_value <= 0:
        return ''
    length = int((value / max_value) * max_width)
    bar = ''
    # nested loop: build bar by appending '#' length times
    for i in range(length):
        bar += '#'
    return bar


def display_chart(projections):
    """Display an ASCII bar chart from projections, showing year and bar.

    projections: list of (year, value)
    """
    if not projections:
        print("No projection data to chart.")
        return

    max_val = max(v for (_, v) in projections)
    print("\nProjected Revenue (ASCII Bar Chart)")
    print("=" * 60)
    for year, val in projections:
        bar = build_bar(val, max_val)
        print(f"Year {year:2d}: {bar}  ${val:,.0f}")
    print("=" * 60 + "\n")


def main():
    projections = get_projection_values()
    display_chart(projections)


if __name__ == '__main__':
    main()
