contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone

    elif choice == "2":
        print("\nContacts:")
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "3":
        break

    else:
        print("Invalid choice")