import tkinter as tk
from tkinter import messagebox
from database import setup_db
from bank import *

setup_db()

# ---------------- APP CLASS ---------------- #
class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Banking App")
        self.root.geometry("500x500")
        self.root.config(bg="#1e1e2f")

        self.user = None

        self.login_screen()

    # ---------------- LOGIN SCREEN ---------------- #
    def login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="🏦 ATM LOGIN", font=("Arial", 18, "bold"),
                 bg="#1e1e2f", fg="white").pack(pady=20)

        self.acc_entry = tk.Entry(self.root)
        self.acc_entry.pack(pady=5)
        self.acc_entry.insert(0, "Account No")

        self.pin_entry = tk.Entry(self.root, show="*")
        self.pin_entry.pack(pady=5)
        self.pin_entry.insert(0, "PIN")

        tk.Button(self.root, text="Login", bg="#4CAF50", fg="white",
                  command=self.login).pack(pady=10)

        tk.Button(self.root, text="Create Account", bg="#2196F3", fg="white",
                  command=self.create_account_screen).pack()

    # ---------------- CREATE ACCOUNT ---------------- #
    def create_account_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Create Account", font=("Arial", 16),
                 bg="#1e1e2f", fg="white").pack(pady=20)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)
        self.name_entry.insert(0, "Name")

        self.new_pin = tk.Entry(self.root)
        self.new_pin.pack(pady=5)
        self.new_pin.insert(0, "PIN")

        tk.Button(self.root, text="Create", bg="green", fg="white",
                  command=self.create_account).pack(pady=10)

        tk.Button(self.root, text="Back", command=self.login_screen).pack()

    def create_account(self):
        name = self.name_entry.get()
        pin = self.new_pin.get()

        acc_no = create_account(name, pin, "saving")
        messagebox.showinfo("Success", f"Account Created!\nAcc No: {acc_no}")

        self.login_screen()

    # ---------------- LOGIN FUNCTION ---------------- #
    def login(self):
        try:
            acc_no = int(self.acc_entry.get())
            pin = self.pin_entry.get()

            self.user = login(acc_no, pin)

            if self.user:
                self.dashboard()
            else:
                messagebox.showerror("Error", "Invalid Login")
        except:
            messagebox.showerror("Error", "Enter valid data")

    # ---------------- DASHBOARD ---------------- #
    def dashboard(self):
        self.clear_screen()

        tk.Label(self.root, text=f"Welcome {self.user.name}",
                 font=("Arial", 16), bg="#1e1e2f", fg="white").pack(pady=10)

        tk.Button(self.root, text="Deposit", width=20, bg="#4CAF50", fg="white",
                  command=self.deposit_screen).pack(pady=5)

        tk.Button(self.root, text="Withdraw", width=20, bg="#f44336", fg="white",
                  command=self.withdraw_screen).pack(pady=5)

        tk.Button(self.root, text="Check Balance", width=20,
                  command=self.show_balance).pack(pady=5)

        tk.Button(self.root, text="Transactions", width=20,
                  command=self.show_transactions).pack(pady=5)

        tk.Button(self.root, text="Logout", width=20,
                  command=self.login_screen).pack(pady=20)

    # ---------------- DEPOSIT ---------------- #
    def deposit_screen(self):
        self.amount_screen("Deposit")

    def withdraw_screen(self):
        self.amount_screen("Withdraw")

    def amount_screen(self, action):
        self.clear_screen()

        tk.Label(self.root, text=f"{action} Amount", font=("Arial", 16),
                 bg="#1e1e2f", fg="white").pack(pady=20)

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=10)

        tk.Button(self.root, text=action, bg="#2196F3", fg="white",
                  command=lambda: self.process_action(action)).pack()

        tk.Button(self.root, text="Back", command=self.dashboard).pack(pady=10)

    def process_action(self, action):
        try:
            amount = float(self.amount_entry.get())

            if action == "Deposit":
                self.user.deposit(amount)
                messagebox.showinfo("Success", "Money Deposited")

            else:
                res = self.user.withdraw(amount)
                if res:
                    messagebox.showerror("Error", res)
                else:
                    messagebox.showinfo("Success", "Money Withdrawn")

            self.dashboard()

        except:
            messagebox.showerror("Error", "Invalid amount")

    # ---------------- BALANCE ---------------- #
    def show_balance(self):
        bal = self.user.get_balance()
        messagebox.showinfo("Balance", f"Your Balance: {bal}")

    # ---------------- TRANSACTIONS ---------------- #
    def show_transactions(self):
        tx = get_transactions(self.user.acc_no)

        text = "\n".join([f"{t[0]}: {t[1]}" for t in tx]) or "No transactions"

        messagebox.showinfo("Transactions", text)

    # ---------------- UTIL ---------------- #
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# ---------------- RUN ---------------- #
root = tk.Tk()
app = BankApp(root)
root.mainloop()