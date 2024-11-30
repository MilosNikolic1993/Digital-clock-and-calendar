import tkinter as tk
from tkinter import ttk
from time import strftime
import datetime

# Funkcija za ažuriranje vremena
def update_time():
    time_string = strftime('%H:%M:%S %p')
    time_label.config(text=time_string)
    time_label.after(1000, update_time)  # Ažuriraj svakih 1000ms

# Funkcija za prikaz datuma
def update_date():
    date_string = datetime.datetime.now().strftime('%A, %d %B %Y')
    date_label.config(text=date_string)

# Kreiranje glavnog prozora
root = tk.Tk()
root.title("Digitalni Sat i Kalendar")

# Prikaz vremena
time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
time_label.pack(anchor='center')

# Prikaz datuma
date_label = tk.Label(root, font=('calibri', 20, 'bold'), background='black', foreground='cyan')
date_label.pack(anchor='center')

# Pokretanje ažuriranja vremena i datuma
update_time()
update_date()

# Pokretanje glavne petlje
root.mainloop()
