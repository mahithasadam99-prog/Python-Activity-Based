
print("ATM Transaction Simulation")

balance = 5000
pin = 1234

entered_pin = int(input("Enter your ATM PIN: "))

if entered_pin == pin:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Available Balance: Rs.", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        if amount > 0:
            balance = balance + amount
            print("Amount Deposited Successfully")
            print("Updated Balance: Rs.", balance)
        else:
            print("Invalid Amount")

    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))
        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Please Collect Your Cash")
            print("Remaining Balance: Rs.", balance)
        else:
            print("Insufficient Balance or Invalid Amount")

    else:
        print("Invalid Choice")

else:
    print("Incorrect PIN")
