
print("Student Performance Trend Analysis")

name = input("Enter student name: ")

m1 = float(input("Enter marks in Test 1: "))
m2 = float(input("Enter marks in Test 2: "))
m3 = float(input("Enter marks in Test 3: "))

average = (m1 + m2 + m3) / 3

print("\n----- PERFORMANCE REPORT -----")
print("Student Name:", name)
print("Test 1 Marks:", m1)
print("Test 2 Marks:", m2)
print("Test 3 Marks:", m3)
print("Average Marks:", round(average, 2))

if m3 > m2 and m2 > m1:
    print("Performance Trend: Improving")
elif m3 < m2 and m2 < m1:
    print("Performance Trend: Declining")
else:
    print("Performance Trend: Fluctuating or Stable")

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: F")
