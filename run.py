import tkinter as tk
from tkinter import ttk
from io import BytesIO
import requests
from PIL import Image, ImageTk
import news  # importuojame jūsų news.py kaip modulį
import weather  # importuojame jūsų weather.py kaip modulį
import nordpool  # importuojame jūsų nordpool.py kaip modulį

# Sukuriame pagrindinį langą
root = tk.Tk()
root.title("Informacijos langas")

# Sukuriame rėmelį pagrindiniame lange
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Nustatome lango dydį
root.geometry("")

# Funkcija užkrauti orų informaciją (naudojame weather.py funkciją)
weather_info, icon_url = weather.get_weather()  # API raktas integruotas weather.py kode
weather_label = ttk.Label(frame, text=weather_info, justify=tk.LEFT, font=("Helvetica", 8))
weather_label.grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)

if icon_url:
    response_icon = requests.get(icon_url)
    icon_data = Image.open(BytesIO(response_icon.content))
    icon_image = ImageTk.PhotoImage(icon_data)
    icon_label = ttk.Label(frame, image=icon_image)
    icon_label.image = icon_image  # išlaikome nuorodą į vaizdą
    icon_label.grid(row=0, column=1, pady=10, padx=10, sticky=tk.W)


# Funkcija užkrauti Nordpool informaciją (naudojame nordpool.py funkciją)
nordpool_info = nordpool.get_nordpool_info()
nordpool_label = ttk.Label(frame, text=nordpool_info, justify=tk.LEFT, font=("Helvetica", 9))
nordpool_label.grid(row=1, column=0, pady=10, padx=10, sticky=tk.W)

# Sukuriame etiketes naujienų atvaizdavimui pagal šaltinius
news_label = ttk.Label(frame, text="15min naujienos:", justify=tk.LEFT, font=("Helvetica", 9, "bold"))
news_label.grid(row=2, column=0, columnspan=2, pady=10, sticky=tk.W)
news_15min = ttk.Label(frame, text=news.get_15min_news(), justify=tk.LEFT, font=("Helvetica", 8))
news_15min.grid(row=3, column=0, columnspan=2, pady=10, sticky=tk.W)

lrt_label = ttk.Label(frame, text="LRT naujienos:", justify=tk.LEFT, font=("Helvetica", 9, "bold"))
lrt_label.grid(row=4, column=0, columnspan=2, pady=10, sticky=tk.W)
news_lrt = ttk.Label(frame, text=news.get_lrt_news(), justify=tk.LEFT, font=("Helvetica", 8))
news_lrt.grid(row=5, column=0, columnspan=2, pady=10, sticky=tk.W)

delfi_label = ttk.Label(frame, text="Delfi naujienos:", justify=tk.LEFT, font=("Helvetica", 9, "bold"))
delfi_label.grid(row=6, column=0, columnspan=2, pady=10, sticky=tk.W)
news_delfi = ttk.Label(frame, text=news.get_delfi_news(), justify=tk.LEFT, font=("Helvetica", 8))
news_delfi.grid(row=7, column=0, columnspan=2, pady=10, sticky=tk.W)

vz_label = ttk.Label(frame, text="Verslo žinios naujienos:", justify=tk.LEFT, font=("Helvetica", 9, "bold"))
vz_label.grid(row=8, column=0, columnspan=2, pady=10, sticky=tk.W)
news_vz = ttk.Label(frame, text=news.get_vz_news(), justify=tk.LEFT, font=("Helvetica", 8))
news_vz.grid(row=9, column=0, columnspan=2, pady=10, sticky=tk.W)

# Pagrindinio lango ciklas
root.mainloop()
