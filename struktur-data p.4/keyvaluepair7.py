user = {"name" : "ajieb","age" : 20,}

# Menggunakan get agar aman dari keyerror
email = user.get("email", "email tidak tersedia")
print("email:", email)

#Menambahkan key jika belum ada dengan setdefault
user.setdefault("email", "ajieb@example.com")

#menghapus key
age = user.pop("age")

#menampilkan semua key-value pair
print(user.keys())
print(user.values())

#menyalin dictionary
user_copy = user.copy()
print(user_copy)

print(user)
print(user_copy)