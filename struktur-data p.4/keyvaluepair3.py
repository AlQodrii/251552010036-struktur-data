# Database pengguna sederhana 
users = {
    "alqodri": "password131006",
    "ajieb": "admin123",
    "aidil": "qwerty123"    
}

# Login Check
username = "alqodri"
password = "password131006"

if username in users and users[username] == password:
    print("Login berhasil!")
else:
    print("Login gagal! Periksa username dan password Anda.")