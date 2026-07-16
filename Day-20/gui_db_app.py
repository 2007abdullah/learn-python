import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ---------------- DATABASE ---------------- #
conn = sqlite3.connect("app.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")
conn.commit()

# ---------------- FUNCTIONS ---------------- #

def add_user():
    name = entry_name.get()
    age = entry_age.get()

    if name == "" or age == "":
        messagebox.showwarning("Error", "Please fill all fields")
        return

    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

    messagebox.showinfo("Success", "User Added Successfully")

    clear_fields()
    show_users()


def show_users():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)


def delete_user():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning("Error", "Select a user to delete")
        return

    user_id = tree.item(selected[0])['values'][0]

    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()

    messagebox.showinfo("Deleted", "User Deleted")
    show_users()


def search_user():
    name = entry_search.get()

    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)


def clear_fields():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("User Management App")
root.geometry("600x500")
root.config(bg="#1e1e2f")

title = tk.Label(root, text="User Management System", 
                 font=("Arial", 16, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=10)

# Form Frame
form_frame = tk.Frame(root, bg="#1e1e2f")
form_frame.pack(pady=10)

tk.Label(form_frame, text="Name:", bg="#1e1e2f", fg="white").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(form_frame)
entry_name.grid(row=0, column=1, padx=5)

tk.Label(form_frame, text="Age:", bg="#1e1e2f", fg="white").grid(row=1, column=0, padx=5, pady=5)
entry_age = tk.Entry(form_frame)
entry_age.grid(row=1, column=1, padx=5)

btn_add = tk.Button(form_frame, text="Add User", bg="#4CAF50", fg="white", command=add_user)
btn_add.grid(row=2, column=0, columnspan=2, pady=10)

# Search
search_frame = tk.Frame(root, bg="#1e1e2f")
search_frame.pack()

entry_search = tk.Entry(search_frame)
entry_search.grid(row=0, column=0, padx=5)

btn_search = tk.Button(search_frame, text="Search", bg="#2196F3", fg="white", command=search_user)
btn_search.grid(row=0, column=1)

btn_show = tk.Button(search_frame, text="Show All", bg="#9C27B0", fg="white", command=show_users)
btn_show.grid(row=0, column=2, padx=5)

# Table
columns = ("ID", "Name", "Age")

tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)

tree.pack(pady=20, fill="both", expand=True)

# Scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Delete Button
btn_delete = tk.Button(root, text="Delete Selected", bg="red", fg="white", command=delete_user)
btn_delete.pack(pady=10)

# Load data on start
show_users()

root.mainloop()