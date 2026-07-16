import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "YOUR_API_KEY_HERE"

# ---------------- FUNCTION ---------------- #
def get_weather():
    city = entry_city.get()

    if city == "":
        messagebox.showwarning("Error", "Enter city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found")
            return

        name = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        result.config(
            text=f"📍 {name}\n🌡 Temp: {temp}°C\n💧 Humidity: {humidity}%\n☁ Condition: {weather}"
        )

    except:
        messagebox.showerror("Error", "Network error")

# ---------------- MULTI CITY ---------------- #
def add_city():
    city = entry_city.get()

    if city == "":
        return

    listbox.insert(tk.END, city)
    entry_city.delete(0, tk.END)

def show_selected_city(event):
    selected = listbox.get(listbox.curselection())
    entry_city.delete(0, tk.END)
    entry_city.insert(0, selected)
    get_weather()

# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("Weather App Pro")
root.geometry("400x500")
root.config(bg="#1e1e2f")

tk.Label(root, text="🌦 Weather App", font=("Arial", 18, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=10)

entry_city = tk.Entry(root)
entry_city.pack(pady=5)

tk.Button(root, text="Get Weather", bg="#4CAF50", fg="white",
          command=get_weather).pack(pady=5)

tk.Button(root, text="Add City", bg="#2196F3", fg="white",
          command=add_city).pack(pady=5)

# Listbox for multiple cities
listbox = tk.Listbox(root)
listbox.pack(pady=10, fill="both", expand=True)
listbox.bind("<<ListboxSelect>>", show_selected_city)

result = tk.Label(root, text="", font=("Arial", 12),
                  bg="#1e1e2f", fg="white", justify="left")
result.pack(pady=10)


root.mainloop()



