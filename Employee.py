name = input("Enter employee name: ")
salary = float(input("Enter basic salary: "))

hra = salary * 0.20
da = salary * 0.10
gross_salary = salary + hra + da

print("\nEmployee Name:", name)
print("Basic Salary:", salary)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross_salary)
