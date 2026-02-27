# Database pengguna
users = {
    "alqodri": "password131006",
    "fabian": "admin123",
    "aidil": "qwerty123"    
}

# Daftar login yang ingin dicek
login_attempts = [
    ("alqodri", "password131006"),
    ("fabiana", "salahpassword"),
    ("aidil", "qwerty123")
]

#cek semua login
for username, password in login_attempts:
    if username in users and users[username] == password:
        print(f"Login {username} berhasil!")
    else:
        print(f"Login {username} gagal! Periksa username dan password Anda.")