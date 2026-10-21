
print("Progressive Water Tariff Analysis")

units = float(input("Enter water consumption units: "))

if units < 0:
    print("Invalid water consumption")
else:
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + (units - 100) * 3
    elif units <= 300:
        bill = (100 * 2) + (100 * 3) + (units - 200) * 5
    else:
        bill = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 8

    print("\n----- WATER BILL -----")
    print("Water Consumption:", units, "units")
    print("Total Water Bill: Rs.", round(bill, 2))
