name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = int(input("Enter marks for subject " + str(i) + ": "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

print("\n===== STUDENT RESULT =====")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")
