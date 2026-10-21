
print("Smart Parking Fee Management")

vehicle = input("Enter vehicle type (car/bike): ").lower()
hours = int(input("Enter parking hours: "))

if hours <= 0:
    print("Invalid parking hours")

elif vehicle == "bike":
    if hours <= 2:
        fee = hours * 10
    else:
        fee = 20 + (hours - 2) * 5

    print("Vehicle Type: Bike")
    print("Parking Fee: Rs.", fee)

elif vehicle == "car":
    if hours <= 2:
        fee = hours * 20
    else:
        fee = 40 + (hours - 2) * 10

    print("Vehicle Type: Car")
    print("Parking Fee: Rs.", fee)

else:
    print("Invalid vehicle type")
