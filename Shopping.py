print("===== SHOPPING BILL =====")

item1 = input("Enter first item: ")
price1 = float(input("Enter price: "))

item2 = input("Enter second item: ")
price2 = float(input("Enter price: "))

item3 = input("Enter third item: ")
price3 = float(input("Enter price: "))

total = price1 + price2 + price3

if total >= 1000:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

print("\n===== BILL =====")
print(item1, ":", price1)
print(item2, ":", price2)
print(item3, ":", price3)
print("Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)
