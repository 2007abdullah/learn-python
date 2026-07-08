password = input("Enter password: ")

if len(password) < 6:
    print("Weak password")

elif password.isdigit():
    print("Password should not be only numbers")

elif password.isalpha():
    print("Add numbers for strong password")

else:
    print("Strong password")