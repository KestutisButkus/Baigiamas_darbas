from datetime import datetime, timedelta, timezone
import requests


# Funkcija gauti duomenis iš API
def gauti_duomenis():
    try:
        url = "https://api.meteo.lt/v1/places/vilnius/forecasts/long-term"
        response = requests.get(url)
        response.raise_for_status()  # Patikrina, ar nėra HTTP klaidų
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Klaida gaunant duomenis: {e}")
        return None


# Funkcija grupuoti dienos ir nakties prognozes
def grupuoti_dienos_nakties_prognozes(data):
    rytojaus_data = (datetime.now(timezone.utc) + timedelta(days=1)).strftime('%Y-%m-%d')
    diena, naktis = [], []
    for forecast in data.get("forecastTimestamps", []):
        laikas = forecast["forecastTimeUtc"]
        temperatura = forecast["airTemperature"]
        busena = forecast["conditionCode"]
        valanda = int(laikas[11:13])  # Išskiriame valandą

        if laikas.startswith(rytojaus_data):
            if 8 <= valanda < 20:
                diena.append((laikas, temperatura, busena))
            else:
                naktis.append((laikas, temperatura, busena))

    return diena, naktis


# Funkcija rasti aukščiausią dienos ir žemiausią nakties temperatūrą
def rasti_extremas(diena, naktis):
    auksciausia_dienos = max(diena, key=lambda x: x[1], default=None)
    zemiausia_nakties = min(naktis, key=lambda x: x[1], default=None)
    return auksciausia_dienos, zemiausia_nakties


# Pagrindinė vykdymo dalis
data = gauti_duomenis()
if data:
    diena, naktis = grupuoti_dienos_nakties_prognozes(data)
    auksciausia_dienos, zemiausia_nakties = rasti_extremas(diena, naktis)

    print("Rezultatai:")
    if auksciausia_dienos:
        print(f"Dienos aukščiausia temperatūra: {auksciausia_dienos[1]}°C, "
              f"laikas: {auksciausia_dienos[0]}, būklė: {auksciausia_dienos[2]}")
    else:
        print("Dienos temperatūros duomenų nėra.")

    if zemiausia_nakties:
        print(f"Nakties žemiausia temperatūra: {zemiausia_nakties[1]}°C, "
              f"laikas: {zemiausia_nakties[0]}, būklė: {zemiausia_nakties[2]}")
    else:
        print("Nakties temperatūros duomenų nėra.")
