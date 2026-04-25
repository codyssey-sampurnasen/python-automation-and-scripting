import requests

# Your API key here
API_KEY = "your_api_key_here"

# City name
city = input("Enter city name: ")

# API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Request data
response = requests.get(url)
data = response.json()

# Check if city found
if data["cod"] != 200:
    print("City not found!")
else:
    # Extract data
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {weather}")
    print(f"Humidity: {humidity}%")
