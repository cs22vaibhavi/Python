text = input("Enter a word or sentence: ")

vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count = count + 1

print("Text:", text)
print("Number of vowels:", count)
