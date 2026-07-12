import requests
import datetime

city = input("Enter city: ")

url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)
data = response.json()

temp = data["current_condition"][0]["temp_C"]
weather = data["current_condition"][0]["weatherDesc"][0]["value"]
now = datetime.datetime.now()


print(now)
print(f"\n🌍 Weather Report for {city}")
print(f"🌡️ Temperature: {temp}°C")
print(f"☁️ Condition: {weather}")