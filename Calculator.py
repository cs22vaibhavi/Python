print("----- Simple Calculator -----")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    result = a + b
    print("Addition =", result)

elif choice == 2:
    result = a - b
    print("Subtraction =", result)

elif choice == 3:
    result = a * b
    print("Multiplication =", result)

elif choice == 4:
    if b != 0:
        result = a / b
        print("Division =", result)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid choice")
