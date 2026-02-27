# Database pengguna
users = {
    "alqodri": "password131006",
    "ajieb": "admin123",
    "aidil": "qwerty123"    
}

print("=== Login Manual ===")
input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")

if input_username in users and users[input_username] == input_password:
    print(f"Login {input_username} berhasil!")
else:
    print(f"Login {input_username} gagal! Periksa username dan password Anda.")