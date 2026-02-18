def get_supply_chain_data():
    """Get warehouse and inventory data from user or use sample data."""
    print("Simple Supply Chain Tracker")
    print("=" * 70)
    print("Build your supply chain inventory.\n")
    
    warehouses = []
    
    while True:
        warehouse_name = input("Enter warehouse name (or 'done' to finish): ").strip()
        if warehouse_name.lower() == 'done':
            break
        if not warehouse_name:
            print("Please enter a valid warehouse name.\n")
            continue
        
        inventory = {}
        print(f"Enter inventory for {warehouse_name}:")
        
        while True:
            product = input(f"  Product name (or 'done' to finish {warehouse_name}): ").strip().lower()
            if product == 'done':
                break
            if not product:
                print("  Please enter a valid product name.")
                continue
            
            try:
                quantity = float(input(f"  {product} quantity: "))
                if quantity < 0:
                    print("  Quantity cannot be negative.")
                    continue
                inventory[product] = quantity
                print(f"  {product}: {quantity} units added.\n")
            except ValueError:
                print("  Invalid input. Please enter a valid number.\n")
        
        if inventory:
            warehouses.append({
                "name": warehouse_name,
                "inventory": inventory
            })
            print(f"{warehouse_name} added to supply chain.\n")
        else:
            print(f"No inventory for {warehouse_name}. Skipping.\n")
    
    # Use sample data if none entered
    if not warehouses:
        print("No warehouse data entered. Using sample data.\n")
        warehouses = [
            {
                "name": "Warehouse A",
                "inventory": {
                    "apples": 100,
                    "bananas": 150,
                    "oranges": 200,
                    "grapes": 75
                }
            },
            {
                "name": "Warehouse B",
                "inventory": {
                    "apples": 200,
                    "bananas": 100,
                    "oranges": 150,
                    "grapes": 120
                }
            },
            {
                "name": "Warehouse C",
                "inventory": {
                    "apples": 150,
                    "bananas": 200,
                    "oranges": 100,
                    "grapes": 90
                }
            }
        ]
    
    return warehouses


def calculate_product_total(warehouses, product):
    """Calculate total stock of a specific product across all warehouses."""
    total = 0
    # Nested loop through warehouses and their inventories
    for warehouse in warehouses:
        inventory = warehouse["inventory"]
        if product in inventory:
            total += inventory[product]
    return total


def get_all_products(warehouses):
    """Get list of all unique products across all warehouses."""
    products = set()
    # Nested loop to collect all products
    for warehouse in warehouses:
        inventory = warehouse["inventory"]
        for product in inventory:
            products.add(product)
    return sorted(list(products))


def calculate_warehouse_total(warehouse):
    """Calculate total units in a single warehouse."""
    total = 0
    for quantity in warehouse["inventory"].values():
        total += quantity
    return total


def calculate_total_supply(warehouses):
    """Calculate total stock across entire supply chain."""
    grand_total = 0
    # Nested loop through all warehouses and products
    for warehouse in warehouses:
        inventory = warehouse["inventory"]
        for quantity in inventory.values():
            grand_total += quantity
    return grand_total


def find_product_location(warehouses, product):
    """Find which warehouses have a specific product."""
    locations = []
    # Nested loop to find product in warehouses
    for warehouse in warehouses:
        if product in warehouse["inventory"]:
            locations.append({
                "warehouse": warehouse["name"],
                "quantity": warehouse["inventory"][product]
            })
    return locations


def find_min_max_stock(warehouses, product):
    """Find warehouse with minimum and maximum stock of a product."""
    locations = find_product_location(warehouses, product)
    
    if not locations:
        return None, None
    
    min_warehouse = min(locations, key=lambda x: x["quantity"])
    max_warehouse = max(locations, key=lambda x: x["quantity"])
    
    return min_warehouse, max_warehouse


def display_warehouse_inventory(warehouses):
    """Display detailed inventory for each warehouse."""
    print("\n" + "=" * 70)
    print("WAREHOUSE INVENTORY DETAILS")
    print("=" * 70)
    
    for warehouse in warehouses:
        name = warehouse["name"]
        inventory = warehouse["inventory"]
        total = calculate_warehouse_total(warehouse)
        
        print(f"\n{name}:")
        print("-" * 70)
        print(f"{'Product':<20} {'Quantity':<15} {'% of Warehouse':<20}")
        print("-" * 70)
        
        for product in sorted(inventory.keys()):
            quantity = inventory[product]
            percentage = (quantity / total * 100) if total > 0 else 0
            print(f"{product.capitalize():<20} {quantity:<15.0f} {percentage:<19.1f}%")
        
        print("-" * 70)
        print(f"{'WAREHOUSE TOTAL':<20} {total:<15.0f}")


def display_supply_chain_summary(warehouses):
    """Display supply chain summary with totals by product."""
    if not warehouses:
        print("No warehouse data to display.")
        return
    
    all_products = get_all_products(warehouses)
    total_supply = calculate_total_supply(warehouses)
    
    print("\n" + "=" * 70)
    print("SUPPLY CHAIN SUMMARY")
    print("=" * 70)
    print(f"{'Product':<20} {'Total Stock':<20} {'Warehouses':<15} {'% of Total':<15}")
    print("-" * 70)
    
    # Loop through all products and show totals
    for product in all_products:
        total = calculate_product_total(warehouses, product)
        locations = find_product_location(warehouses, product)
        num_warehouses = len(locations)
        percentage = (total / total_supply * 100) if total_supply > 0 else 0
        
        print(f"{product.capitalize():<20} {total:<20.0f} {num_warehouses:<15} {percentage:<14.1f}%")
    
    print("-" * 70)
    print(f"{'TOTAL INVENTORY':<20} {total_supply:<20.0f}")
    print("=" * 70 + "\n")


def display_warehouse_summary(warehouses):
    """Display summary of each warehouse's total stock."""
    print("\n" + "=" * 70)
    print("WAREHOUSE SUMMARY")
    print("=" * 70)
    print(f"{'Warehouse':<25} {'Total Units':<20} {'# Products':<15}")
    print("-" * 70)
    
    total_supply = calculate_total_supply(warehouses)
    
    for warehouse in warehouses:
        name = warehouse["name"]
        total = calculate_warehouse_total(warehouse)
        num_products = len(warehouse["inventory"])
        percentage = (total / total_supply * 100) if total_supply > 0 else 0
        
        print(f"{name:<25} {total:<20.0f} {num_products:<15}")
    
    print("-" * 70)
    print(f"{'GRAND TOTAL':<25} {total_supply:<20.0f}")
    print("=" * 70 + "\n")


def search_product(warehouses):
    """Search for a specific product across the supply chain."""
    all_products = get_all_products(warehouses)
    
    if not all_products:
        print("No products in supply chain.")
        return
    
    print("\nAvailable products:", ", ".join(p.capitalize() for p in all_products))
    product = input("\nEnter product to search: ").strip().lower()
    
    locations = find_product_location(warehouses, product)
    
    if not locations:
        print(f"Product '{product}' not found in any warehouse.")
        return
    
    total = sum(loc["quantity"] for loc in locations)
    min_stock, max_stock = find_min_max_stock(warehouses, product)
    
    print(f"\n{product.upper()} INVENTORY")
    print("=" * 70)
    for loc in locations:
        print(f"{loc['warehouse']:<25} {loc['quantity']:<20.0f} units")
    
    print("-" * 70)
    print(f"Total: {total:.0f} units")
    print(f"Min stock: {min_stock['warehouse']} ({min_stock['quantity']:.0f} units)")
    print(f"Max stock: {max_stock['warehouse']} ({max_stock['quantity']:.0f} units)")
    print("=" * 70 + "\n")


def main():
    """Main function to run the supply chain tracker."""
    warehouses = get_supply_chain_data()
    
    while True:
        print("\nSupply Chain Tracker Menu")
        print("-" * 40)
        print("1. View Supply Chain Summary")
        print("2. View Warehouse Summary")
        print("3. View Warehouse Details")
        print("4. Search Product")
        print("5. Exit")
        print("-" * 40)
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == '1':
            display_supply_chain_summary(warehouses)
        elif choice == '2':
            display_warehouse_summary(warehouses)
        elif choice == '3':
            display_warehouse_inventory(warehouses)
        elif choice == '4':
            search_product(warehouses)
        elif choice == '5':
            print("Thank you for using the Supply Chain Tracker!")
            break
        else:
            print("Invalid option. Please select 1-5.")


if __name__ == "__main__":
    main()
