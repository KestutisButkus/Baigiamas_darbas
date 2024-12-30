import json
import requests

place = "Žiegždriai"
url = f"https://api.meteo.lt/v1/places/{place}/forecasts/long-term"

# Atliksime GET užklausą
response = requests.get(url)

if response.status_code == 200:
    # Konvertuojame atsakymą į JSON formatą
    data = response.json()
    print(json.dumps(data, indent=4))

    location = data['place']['name']  # Vietovė
    temp_now = data["forecastTimestamps"][0]["airTemperature"]  # Dabartinė temperatūra
    temp_feel = data["forecastTimestamps"][0]["feelsLikeTemperature"]  # Jaučiama temperatūra
    wind_speed = data["forecastTimestamps"][0]["windSpeed"]  # Vėjo greitis
    wind_gust = data["forecastTimestamps"][0]["windGust"]  # Vėjo gūsiai
    wind_degree = data["forecastTimestamps"][0]["windDirection"]  # Vėjo kryptis (laipsniais)
    cloud_cover = data["forecastTimestamps"][0]["cloudCover"]  # Debesuotumas
    pressure_hpa = data["forecastTimestamps"][0]["seaLevelPressure"]  # Slėgis jūros lygyje
    hpa_to_mmhg = 0.75006  # Konversijos koeficientas naudojamas atmosferos slėgio matavimo vienetų konvertavimui.
    pressure_mmhg = pressure_hpa * hpa_to_mmhg  # Slėgis jūros lygyje "Torr"
    relative_humidity = data["forecastTimestamps"][0]["relativeHumidity"]  # Santykinė drėgmė
    total_precipitation = data["forecastTimestamps"][0]["totalPrecipitation"]  # Krituliai
    condition_code = data["forecastTimestamps"][0]["conditionCode"]  # Orų būklė

    if 350 <= wind_degree < 10:
        wind_direction = 'N'
    elif 10 <= wind_degree < 80:
        wind_direction = 'NE'
    elif 80 <= wind_degree < 100:
        wind_direction = 'E'
    elif 100 <= wind_degree < 170:
        wind_direction = 'SE'
    elif 170 <= wind_degree < 190:
        wind_direction = 'S'
    elif 190 <= wind_degree < 260:
        wind_direction = 'SW'
    elif 260 <= wind_degree < 280:
        wind_direction = 'W'
    else:
        wind_direction = 'NW'

    print(f"Vieta: {location}")
    print(f"Dabartinė temperatūra: {temp_now} °C")
    print(f"Jaučiama temperatūra: {temp_feel} °C")
    print(f"Vėjo greitis: {wind_speed} m/s")
    print(f"Vėjo gūsiai: {wind_gust} m/s")
    print(f"Vėjo kryptis: {wind_degree} ° {wind_direction}")
    print(f"Debesuotumas: {cloud_cover}%")
    print(f"Slėgis jūros lygyje: {pressure_hpa} hPa, {pressure_mmhg:.0f} mmHg(Torr)")
    print(f"Santykinė drėgmė: {relative_humidity}%")
    print(f"Krituliai: {total_precipitation} mm")
    print(f"Orų būklė: {condition_code}")
