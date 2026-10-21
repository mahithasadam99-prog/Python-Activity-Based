name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

print("\nPatient Classification")
if age < 18:
    print("Patient Type: Child")
elif age >= 60:
    print("Patient Type: Senior Citizen")
else:
    print("Patient Type: Adult")

print("\nHospital Billing")
print("1. General Ward - Rs. 1000")
print("2. Special Ward - Rs. 2000")
print("3. ICU - Rs. 5000")

choice = int(input("Enter ward choice (1-3): "))
days = int(input("Enter number of days: "))

if choice == 1:
    bill = 1000 * days
elif choice == 2:
    bill = 2000 * days
elif choice == 3:
    bill = 5000 * days
else:
    bill = 0
    print("Invalid ward choice!")

if bill > 0:
    print("\n--- Hospital Bill ---")
    print("Patient Name:", name)
    print("Total Days:", days)
    print("Total Bill: Rs.", bill)
