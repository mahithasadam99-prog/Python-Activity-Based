
name = input("Enter customer name: ")
amount = float(input("Enter total purchase amount: "))
discount = 0

if amount >= 5000:
    discount = 20
elif amount >= 3000:
    discount = 15
elif amount >= 1000:
    discount = 10
else:
    discount = 0

discount_amount = amount * discount / 100
final_amount = amount - discount_amount

print("\n----- RETAIL BILL -----")
print("Customer Name:", name)
print("Purchase Amount: Rs.", amount)
print("Discount:", discount, "%")
print("Discount Amount: Rs.", discount_amount)
print("Final Bill Amount: Rs.", final_amount)
