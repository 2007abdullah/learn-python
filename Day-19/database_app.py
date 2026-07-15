import sqlite3

conn1 = sqlite3.connect("users.db")
cursor = conn1.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

while True:
    print("\n1. Add User")
    print("2. Show Users")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        conn1.commit()

    elif choice == "2":
        cursor.execute("SELECT * FROM users")
        for user in cursor.fetchall():
            print(user)

    elif choice == "3":
        break