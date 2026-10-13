import requests
import csv

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": -23.55,
    "longitude": -46.63,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "past_days": 7,
    "forecast_days": 1,
    "timezone": "America/Sao_Paulo"
}


response = requests.get(url, params=params)

response.raise_for_status()

data = response.json()

daily = data["daily"]

dates = daily["time"]
temperature_max = daily["temperature_2m_max"]
temperature_min = daily["temperature_2m_min"]
precipitation = daily["precipitation_sum"]

print(dates)
print(temperature_max)
print(temperature_min)
print(precipitation)

print(len(dates))


with open("weather_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "date",
        "temperature_max",
        "temperature_min",
        "precipitation"
    ])

    for i in range(len(dates)):
         writer.writerow([
            dates[i],
            temperature_max[i],
            temperature_min[i],
            precipitation[i]
        ])


         

