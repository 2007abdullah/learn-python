import smtplib

sender = "abdullahhyaat@gmail.com"
password = "efyo fzvv dfto dapu"

emails = ["saleemkhan7476@gmail.com", "tasleembloach2009@gmail.com"]

subject = "Hello"
body = "This is a test email from Python"

message = f"Subject: {subject}\n\n{body}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)

for email in emails:
    server.sendmail(sender, email, message)
    print("Sent to", email)

server.quit()