import customtkinter as ctk
from datetime import datetime
from openai import OpenAI

# 🔐 ADD YOUR API KEY
client = OpenAI(api_key="YOUR_API_KEY")

ctk.set_appearance_mode("dark")

# 🧠 MEMORY (conversation history)
chat_history = []

# 🚀 MAIN APP
app = ctk.CTk()
app.geometry("400x600")
app.title("WhatsApp AI Clone")

# 💬 CHAT FRAME
chat_frame = ctk.CTkScrollableFrame(app)
chat_frame.pack(fill="both", expand=True, padx=10, pady=10)

# ✏️ INPUT
entry = ctk.CTkEntry(app, placeholder_text="Type a message...")
entry.pack(fill="x", padx=10, pady=5)

# 📩 ADD MESSAGE (BUBBLE STYLE)
def add_message(msg, sender="user"):
    time = datetime.now().strftime("%H:%M")

    if sender == "user":
        bubble = ctk.CTkLabel(
            chat_frame,
            text=f"{msg}\n{time} ✔✔",
            fg_color="#25D366",
            text_color="black",
            corner_radius=10,
            justify="right",
            anchor="e",
            padx=10,
            pady=5
        )
        bubble.pack(anchor="e", pady=5)

    else:
        bubble = ctk.CTkLabel(
            chat_frame,
            text=f"{msg}\n{time}",
            fg_color="#262D31",
            text_color="white",
            corner_radius=10,
            justify="left",
            anchor="w",
            padx=10,
            pady=5
        )
        bubble.pack(anchor="w", pady=5)

# 🤖 AI RESPONSE
def get_ai_reply(user_msg):
    chat_history.append({"role": "user", "content": user_msg})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history
    )

    reply = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": reply})

    return reply

# 📤 SEND FUNCTION
def send():
    user_msg = entry.get()
    if user_msg.strip() == "":
        return

    add_message(user_msg, "user")
    entry.delete(0, "end")

    # AI reply
    reply = get_ai_reply(user_msg)
    add_message(reply, "bot")

# 🔘 SEND BUTTON
send_btn = ctk.CTkButton(app, text="Send", command=send)
send_btn.pack(pady=10)

# ⌨️ ENTER KEY
app.bind("<Return>", lambda event: send())

app.mainloop()