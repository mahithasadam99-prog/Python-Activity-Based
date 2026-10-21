
print("Railway Fare and Reservation Calculator")

name = input("Enter passenger name: ")
age = int(input("Enter passenger age: "))

print("\nSelect Travel Class")
print("1. Sleeper - Rs. 200")
print("2. AC 3 Tier - Rs. 500")
print("3. AC 2 Tier - Rs. 800")

choice = int(input("Enter class choice (1-3): "))
distance = float(input("Enter distance in km: "))

if choice == 1:
    rate = 1
    class_name = "Sleeper"
elif choice == 2:
    rate = 2
    class_name = "AC 3 Tier"
elif choice == 3:
    rate = 3
    class_name = "AC 2 Tier"
else:
    rate = 0
    class_name = "Invalid"

if rate > 0 and distance > 0:
    if choice == 1:
        fare = distance * 1
    elif choice == 2:
        fare = distance * 2
    else:
        fare = distance * 3

    if age < 5:
        fare = 0
    elif age >= 60:
        fare = fare * 0.9

    reservation_charge = 50
    total = fare + reservation_charge

    print("\n----- RAILWAY TICKET -----")
    print("Passenger Name:", name)
    print("Passenger Age:", age)
    print("Travel Class:", class_name)
    print("Distance:", distance, "km")
    print("Ticket Fare: Rs.", round(fare, 2))
    print("Reservation Charge: Rs.", reservation_charge)
    print("Total Fare: Rs.", round(total, 2))
else:
    print("Invalid class choice or distance")
