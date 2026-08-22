num = int(input("Enter a number: "))

print("Multiplication Table")

for i in range(1, 11):
    result = num * i
    print(num, "x", i, "=", result)
