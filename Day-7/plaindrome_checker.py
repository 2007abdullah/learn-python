text = input("Enter word: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")