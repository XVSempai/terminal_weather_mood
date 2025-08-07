import requests
import sys

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C"
    response = requests.get(url)
    return response.text.strip()

def mood_for(weather):
    moods = {
        "Sunny": "☀️ It's sunny — go outside and smile 😎",
        "Clear": "🌟 Clear skies — make the most of it 🌈",
        "Partly cloudy": "⛅ Take a deep breath and enjoy the day",
        "Cloudy": "☁️ Cloudy — perfect for tea and reflection ☕",
        "Rain": "🌧️ Rainy — maybe write some code? 👨‍💻",
        "Snow": "❄️ Snowy — build a snowman in your heart ⛄",
        "Thunderstorm": "⛈️ Stormy — stay safe and creative 🔌",
    }
    return moods.get(weather, f"🤔 Weather is {weather} — you decide the mood!")

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "--city":
        print("Usage: weathermood --city CityName")
        return
    city = sys.argv[2]
    weather = get_weather(city)
    print(mood_for(weather))

if __name__ == "__main__":
    main()
