name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

total = maths + science + english
average = total / 3

print("\nStudent Name:", name)
print("Maths:", maths)
print("Science:", science)
print("English:", english)
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
