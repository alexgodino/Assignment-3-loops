def get_loan_data():
    """Get loan details from user or use sample data."""
    print("Bank Loan Repayment Simulator")
    print("=" * 60)
    print("Enter your loan details.\n")
    
    try:
        loan_amount = float(input("Loan amount: $"))
        if loan_amount <= 0:
            print("Loan amount must be positive. Using sample data.\n")
            return get_sample_data()
        
        annual_rate = float(input("Annual interest rate (%): "))
        if annual_rate < 0:
            print("Interest rate cannot be negative. Using sample data.\n")
            return get_sample_data()
        
        monthly_payment = float(input("Monthly payment amount: $"))
        if monthly_payment <= 0:
            print("Monthly payment must be positive. Using sample data.\n")
            return get_sample_data()
        
        return {
            "principal": loan_amount,
            "annual_rate": annual_rate,
            "monthly_payment": monthly_payment
        }
    except ValueError:
        print("Invalid input. Using sample data.\n")
        return get_sample_data()


def get_sample_data():
    """Return sample loan data."""
    return {
        "principal": 10000,
        "annual_rate": 5.5,
        "monthly_payment": 300
    }


def get_monthly_rate(annual_rate):
    """Convert annual interest rate to monthly decimal rate."""
    return annual_rate / 100 / 12


def calculate_monthly_interest(balance, monthly_rate):
    """Calculate interest charged for the month."""
    return balance * monthly_rate


def apply_payment(balance, monthly_payment, monthly_interest):
    """Apply payment to balance after adding interest."""
    new_balance = balance + monthly_interest - monthly_payment
    return new_balance


def validate_payment_feasibility(principal, monthly_payment, monthly_rate):
    """Check if monthly payment is sufficient to pay off the loan."""
    monthly_interest = principal * monthly_rate
    if monthly_payment < monthly_interest:
        return False
    return True


def simulate_repayment(principal, annual_rate, monthly_payment):
    """Simulate month-by-month loan repayment using a while loop."""
    monthly_rate = get_monthly_rate(annual_rate)
    
    # Check if payment is feasible
    if not validate_payment_feasibility(principal, monthly_payment, monthly_rate):
        return None
    
    balance = principal
    month = 0
    payment_schedule = []
    total_interest = 0
    
    # While loop to simulate each month
    while balance > 0:
        month += 1
        monthly_interest = calculate_monthly_interest(balance, monthly_rate)
        total_interest += monthly_interest
        
        # Adjust final payment if remaining balance is less than monthly payment
        if balance + monthly_interest < monthly_payment:
            final_payment = balance + monthly_interest
            balance = 0
        else:
            final_payment = monthly_payment
            balance = apply_payment(balance, monthly_payment, monthly_interest)
        
        # Store payment details for schedule
        payment_schedule.append({
            "month": month,
            "payment": final_payment,
            "interest": monthly_interest,
            "principal_paid": final_payment - monthly_interest,
            "remaining_balance": max(balance, 0)  # Ensure no negative balance
        })
    
    return {
        "months": month,
        "total_paid": principal + total_interest,
        "total_interest": total_interest,
        "schedule": payment_schedule
    }


def get_total_paid(schedule):
    """Calculate total amount paid."""
    return sum(payment["payment"] for payment in schedule)


def get_total_interest_paid(principal, total_paid):
    """Calculate total interest paid."""
    return total_paid - principal


def display_repayment_summary(loan_data, repayment_data):
    """Display summary of loan repayment."""
    if repayment_data is None:
        print("\n" + "=" * 60)
        print("ERROR: Monthly payment too low!")
        print("=" * 60)
        print(f"Loan amount: ${loan_data['principal']:.2f}")
        print(f"Annual rate: {loan_data['annual_rate']:.2f}%")
        print(f"Monthly payment: ${loan_data['monthly_payment']:.2f}")
        
        monthly_rate = get_monthly_rate(loan_data['annual_rate'])
        min_payment = loan_data['principal'] * monthly_rate
        print(f"Minimum payment (interest only): ${min_payment:.2f}")
        print("Increase monthly payment to at least the minimum required.\n")
        return
    
    print("\n" + "=" * 60)
    print("LOAN REPAYMENT SUMMARY")
    print("=" * 60)
    print(f"Loan amount: ${loan_data['principal']:.2f}")
    print(f"Annual interest rate: {loan_data['annual_rate']:.2f}%")
    print(f"Monthly payment: ${loan_data['monthly_payment']:.2f}")
    print("-" * 60)
    print(f"Months to pay off: {repayment_data['months']}")
    print(f"Total amount paid: ${repayment_data['total_paid']:.2f}")
    print(f"Total interest paid: ${repayment_data['total_interest']:.2f}")
    print(f"Interest as % of principal: {(repayment_data['total_interest'] / loan_data['principal'] * 100):.2f}%")
    print("=" * 60 + "\n")


def display_payment_schedule(repayment_data, show_all=False):
    """Display detailed payment schedule."""
    if repayment_data is None:
        return
    
    schedule = repayment_data["schedule"]
    
    print("PAYMENT SCHEDULE")
    print("-" * 80)
    print(f"{'Month':<8} {'Payment':<15} {'Interest':<15} {'Principal':<15} {'Balance':<15}")
    print("-" * 80)
    
    # Show first 12 months and last few months, or all if requested
    if show_all or len(schedule) <= 24:
        for payment in schedule:
            print(f"{payment['month']:<8} ${payment['payment']:<14.2f} ${payment['interest']:<14.2f} "
                  f"${payment['principal_paid']:<14.2f} ${payment['remaining_balance']:<14.2f}")
    else:
        # Show first 12 months
        for i in range(min(12, len(schedule))):
            payment = schedule[i]
            print(f"{payment['month']:<8} ${payment['payment']:<14.2f} ${payment['interest']:<14.2f} "
                  f"${payment['principal_paid']:<14.2f} ${payment['remaining_balance']:<14.2f}")
        
        # Show ellipsis
        print(f"{'...':<8} {'...':<15} {'...':<15} {'...':<15} {'...':<15}")
        
        # Show last 3 months
        for i in range(max(12, len(schedule) - 3), len(schedule)):
            payment = schedule[i]
            print(f"{payment['month']:<8} ${payment['payment']:<14.2f} ${payment['interest']:<14.2f} "
                  f"${payment['principal_paid']:<14.2f} ${payment['remaining_balance']:<14.2f}")
    
    print("-" * 80 + "\n")


def main():
    """Main function to run the loan repayment simulator."""
    loan_data = get_loan_data()
    
    print(f"\nSimulating repayment with:")
    print(f"  Principal: ${loan_data['principal']:.2f}")
    print(f"  Annual Rate: {loan_data['annual_rate']:.2f}%")
    print(f"  Monthly Payment: ${loan_data['monthly_payment']:.2f}\n")
    
    repayment_data = simulate_repayment(
        loan_data['principal'],
        loan_data['annual_rate'],
        loan_data['monthly_payment']
    )
    
    display_repayment_summary(loan_data, repayment_data)
    
    if repayment_data is not None:
        # Ask if user wants to see full schedule
        while True:
            choice = input("Display full payment schedule? (yes/no): ").strip().lower()
            if choice in ['yes', 'y']:
                display_payment_schedule(repayment_data, show_all=True)
                break
            elif choice in ['no', 'n']:
                display_payment_schedule(repayment_data, show_all=False)
                break
            else:
                print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
