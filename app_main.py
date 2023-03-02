import tkinter as tk
from tkinter import ttk
import subprocess

# Lista serwerów
servers = [
# Add sth like:
#   ("server_name", "username", "ip_address"),
]

# Funkcja, która uruchamia program Terminator z poleceniem ssh
def connect_to_server(server):
    command = f"ssh {server[1]}@{server[2]}" # Tworzenie polecenia ssh
    subprocess.Popen(["terminator", "--new-tab", "-e", command]) # Uruchamianie programu Terminator z poleceniem ssh

# Tworzenie interfejsu GUI
root = tk.Tk()
root.title("Lista serwerów")

# Tworzenie ramki
frame = tk.Frame(root)
frame.pack(pady=10)

# Dodawanie nagłówków tabeli do ramki
header_names = ["Nazwa serwera", "Adres IP"]
for i, name in enumerate(header_names):
    label = tk.Label(frame, text=name, font=("bold", 10))
    label.grid(row=0, column=i, padx=10, pady=5)

# Dodawanie listy serwerów do interfejsu
for i, (name, username, ip_address) in enumerate(servers):
    # Dodawanie etykiety z nazwą serwera i adresem IP do ramki
    label_name = tk.Label(frame, text=name)
    label_name.grid(row=i+1, column=0, padx=10, pady=5)
    label_ip = tk.Label(frame, text=ip_address)
    label_ip.grid(row=i+1, column=1, padx=10, pady=5)

    # Dodawanie paska Separator między etykietami
    separator = tk.ttk.Separator(frame, orient="horizontal")
    separator.grid(row=i+2, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

    # Przypisywanie funkcji obsługującej kliknięcie etykiety z nazwą serwera
    label_name.bind("<Button-1>", lambda event, server=(name, username, ip_address): connect_to_server(server))
    label_name.config(cursor="hand2")

# Uruchamianie interfejsu
root.mainloop()