import tkinter as tk
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

# Dodawanie listy serwerów do interfejsu
for i, (name, username, ip_address) in enumerate(servers):
    label = tk.Label(root, text=name)
    label.grid(row=i, column=0, padx=5, pady=5)
    button = tk.Button(root, text="Połącz", command=lambda server=(name, username, ip_address): connect_to_server(server))
    button.grid(row=i, column=1, padx=5, pady=5)

# Uruchamianie interfejsu
root.mainloop()
