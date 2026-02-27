# define initial dictionary so modifications have a target
# structure mirrors keyvaluepair.py

data = {"name": "ajieb",
        "age": 20,
        "city": "jakarta"}

# Menambahkan key-value baru
data["email"] = "ajieb@example.com"

# mengubah value
# (age originally 20, now updated to 21)
data["age"] = 21

# Hasil akhir
print(data)
