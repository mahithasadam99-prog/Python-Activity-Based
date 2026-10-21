
print("Multi-Currency Travel Budget Analysis")

budget = float(input("Enter your travel budget in INR: "))

print("\nSelect destination currency:")
print("1. US Dollar (USD)")
print("2. Euro (EUR)")
print("3. British Pound (GBP)")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    currency = "USD"
    rate = 83
elif choice == 2:
    currency = "EUR"
    rate = 90
elif choice == 3:
    currency = "GBP"
    rate = 105
else:
    currency = ""
    rate = 0
    print("Invalid choice!")

if rate > 0:
    converted_budget = budget / rate

    print("\n----- TRAVEL BUDGET -----")
    print("Budget in INR: Rs.", budget)
    print("Destination Currency:", currency)
    print("Exchange Rate: 1", currency, "=", rate, "INR")
    print("Converted Budget:", round(converted_budget, 2), currency)
