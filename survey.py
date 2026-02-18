def get_survey_data():
    """Get survey data from user or use sample data."""
    print("Market Survey Analyzer")
    print("=" * 40)
    print("Enter customer product preferences.")
    print("Enter 'done' to finish.\n")
    
    preferences = []
    while True:
        product = input("Enter product preference (or 'done' to finish): ").strip().lower()
        if product == 'done':
            break
        if product == '':
            print("Please enter a valid product name.")
            continue
        preferences.append(product)
    
    if not preferences:
        print("\nNo data entered. Using sample data.\n")
        preferences = ["coffee", "tea", "coffee", "soda", "coffee", "tea", "soda", "coffee"]
    
    return preferences


def count_preferences(preferences):
    """Count occurrences of each product preference."""
    preference_counts = {}
    for product in preferences:
        if product in preference_counts:
            preference_counts[product] += 1
        else:
            preference_counts[product] = 1
    return preference_counts


def calculate_percentages(preference_counts, total_surveys):
    """Calculate market share percentage for each product."""
    percentages = {}
    for product, count in preference_counts.items():
        percentage = (count / total_surveys) * 100
        percentages[product] = percentage
    return percentages


def sort_by_preference(preference_counts):
    """Sort products by preference count (descending)."""
    return sorted(preference_counts.items(), key=lambda x: x[1], reverse=True)


def display_market_share(preferences):
    """Display market share summary."""
    if len(preferences) == 0:
        print("No survey data to analyze.")
        return
    
    # Count preferences
    preference_counts = count_preferences(preferences)
    total_surveys = len(preferences)
    
    # Calculate percentages
    percentages = calculate_percentages(preference_counts, total_surveys)
    
    # Sort by preference
    sorted_preferences = sort_by_preference(preference_counts)
    
    # Display results
    print("\n" + "=" * 40)
    print("MARKET SHARE SUMMARY")
    print("=" * 40)
    print(f"Total responses: {total_surveys}\n")
    
    for product, count in sorted_preferences:
        percentage = percentages[product]
        print(f"{product.capitalize():12} {percentage:6.1f}% ({count})")
    
    print("=" * 40 + "\n")


def main():
    """Main function to run the survey analyzer."""
    preferences = get_survey_data()
    display_market_share(preferences)


if __name__ == "__main__":
    main()
