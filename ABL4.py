
print("Examination Result and Grace-Mark Validation")

marks = int(input("Enter your marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks!")
elif marks >= 40:
    print("Result: Pass")
elif marks >= 35:
    grace = 40 - marks
    print("Grace Marks Required:", grace)
    print("Result: Pass with Grace Marks")
else:
    print("Result: Fail")
