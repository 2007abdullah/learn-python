import smtplib
import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import time
import threading
from email.message import EmailMessage
from datetime import datetime

# 🔒 FIXED CREDENTIALS
SENDER_EMAIL = "abdullahhyaat@gmail.com"
APP_PASSWORD = "efyo fzvv dfto dapu"

selected_file = None

# 📩 SEND EMAIL FUNCTION
def send_email(receiver, subject, body, attachment_path=None):
    try:
        msg = EmailMessage()
        msg['From'] = SENDER_EMAIL
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.set_content(body)

        # 📎 Attachment
        if attachment_path:
            with open(attachment_path, "rb") as f:
                file_data = f.read()
                file_name = attachment_path.split("/")[-1]
                msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()

        print(f"Sent to {receiver}")

    except Exception as e:
        print("Error:", e)


# 📩 SINGLE SEND
def send_single():
    receiver = receiver_entry.get()
    subject = subject_entry.get()
    body = message_text.get("1.0", tk.END)

    send_email(receiver, subject, body, selected_file)
    messagebox.showinfo("Success", "Email Sent!")


# 📊 BULK SEND
def send_bulk():
    if not selected_file:
        messagebox.showerror("Error", "Select CSV file first!")
        return

    subject = subject_entry.get()
    body = message_text.get("1.0", tk.END)

    try:
        with open(selected_file, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                email = row[0]
                send_email(email, subject, body)

        messagebox.showinfo("Success", "Bulk Emails Sent!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# 📂 SELECT FILE
def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename()
    file_label.config(text=selected_file)


# ⏰ SCHEDULER (NO EXTERNAL LIB)
def schedule_email():
    time_str = time_entry.get()  # HH:MM
    receiver = receiver_entry.get()
    subject = subject_entry.get()
    body = message_text.get("1.0", tk.END)

    def wait_and_send():
        while True:
            now = datetime.now().strftime("%H:%M")
            if now == time_str:
                send_email(receiver, subject, body, selected_file)
                print("Scheduled email sent!")
                break
            time.sleep(30)  # check every 30 sec

    threading.Thread(target=wait_and_send, daemon=True).start()
    messagebox.showinfo("Scheduled", f"Email will be sent at {time_str}")


# 🎨 GUI
root = tk.Tk()
root.title("Smart Email Automation System")
root.geometry("500x600")

tk.Label(root, text="Receiver Email").pack()
receiver_entry = tk.Entry(root, width=50)
receiver_entry.pack()

tk.Label(root, text="Subject").pack()
subject_entry = tk.Entry(root, width=50)
subject_entry.pack()

tk.Label(root, text="Message").pack()
message_text = tk.Text(root, height=10, width=50)
message_text.pack()

tk.Label(root, text="Schedule Time (HH:MM)").pack()
time_entry = tk.Entry(root)
time_entry.pack()

tk.Button(root, text="Select CSV / Attachment", command=select_file).pack()
file_label = tk.Label(root, text="No file selected")
file_label.pack()

tk.Button(root, text="Send Single Email", command=send_single).pack(pady=5)
tk.Button(root, text="Send Bulk Emails (CSV)", command=send_bulk).pack(pady=5)
tk.Button(root, text="Schedule Email", command=schedule_email).pack(pady=5)

root.mainloop()