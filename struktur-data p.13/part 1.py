import pandas as pd
import matplotlib.pyplot as plt
import os

# Data penjualan selama 6 hari pertama (10 baris)
data = [
    {"Tanggal": "2025-07-01", "Warna": "Merah", "Ukuran": "M", "Jumlah": 2, "Harga": 25000},
    {"Tanggal": "2025-07-01", "Warna": "Putih", "Ukuran": "L", "Jumlah": 1, "Harga": 30000},
    {"Tanggal": "2025-07-02", "Warna": "Hitam", "Ukuran": "XL", "Jumlah": 3, "Harga": 35000},
    {"Tanggal": "2025-07-03", "Warna": "Merah", "Ukuran": "S", "Jumlah": 4, "Harga": 20000},
    {"Tanggal": "2025-07-04", "Warna": "Putih", "Ukuran": "M", "Jumlah": 2, "Harga": 25000},
    {"Tanggal": "2025-07-04", "Warna": "Hitam", "Ukuran": "L", "Jumlah": 1, "Harga": 30000},
    {"Tanggal": "2025-07-05", "Warna": "Merah", "Ukuran": "XL", "Jumlah": 1, "Harga": 35000},
    {"Tanggal": "2025-07-05", "Warna": "Putih", "Ukuran": "S", "Jumlah": 3, "Harga": 20000},
    {"Tanggal": "2025-07-06", "Warna": "Hitam", "Ukuran": "M", "Jumlah": 2, "Harga": 25000},
    {"Tanggal": "2025-07-06", "Warna": "Merah", "Ukuran": "L", "Jumlah": 3, "Harga": 30000},
]


def main():
    df = pd.DataFrame(data)
    # Pastikan tipe tanggal benar
    df["Tanggal"] = pd.to_datetime(df["Tanggal"])

    # Hitung total per baris dan total penjualan
    df["Total"] = df["Jumlah"] * df["Harga"]
    total_penjualan = df["Total"].sum()

    # Urutan warna yang diinginkan dan jumlah terjual per warna
    warna_order = ["Merah", "Putih", "Hitam"]
    warna_terjual = (
        df.groupby("Warna")["Jumlah"].sum().reindex(warna_order).fillna(0).astype(int)
    )

    total_kaos = warna_terjual.sum()

    # Hindari pembagian nol
    if total_kaos == 0:
        probabilitas = pd.Series(0.0, index=warna_terjual.index)
    else:
        probabilitas = (warna_terjual / total_kaos) * 100

    # Output yang lebih rapi
    print("Total Penjualan Selama 6 Hari: Rp {:,.0f}".format(total_penjualan))

    print("\nProbabilitas Warna Paling Sering Dibeli:")
    for warna, prob in probabilitas.items():
        print(f"{warna}: {prob:.2f}%")

    # Visualisasi sederhana
    colors_map = {"Merah": "red", "Putih": "lightgray", "Hitam": "black"}
    bar_colors = [colors_map.get(w, "tab:blue") for w in warna_terjual.index]
    ax = warna_terjual.plot(kind="bar", color=bar_colors)
    ax.set_ylabel("Jumlah Terjual")
    ax.set_title("Penjualan per Warna (6 Hari)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    # Simpan grafik ke file sebelum menampilkan
    try:
        out_path = os.path.join(os.path.dirname(__file__), 'penjualan_warna.png')
        plt.gcf().savefig(out_path, dpi=150)
        print('Saved plot to:', out_path)
    except Exception:
        pass
    plt.show()


if __name__ == "__main__":
    main()

import pandas as pd
import matplotlib.pyplot as plt
import os

# Set headless mode
os.environ['MPLBACKEND'] = 'Agg'

# Data penjualan (dari part 1)
data = [
    {"Tanggal": "2025-07-01", "Warna": "Merah", "Ukuran": "M", "Jumlah": 2, "Harga": 25000},
    {"Tanggal": "2025-07-01", "Warna": "Putih", "Ukuran": "L", "Jumlah": 1, "Harga": 30000},
    {"Tanggal": "2025-07-02", "Warna": "Hitam", "Ukuran": "XL", "Jumlah": 3, "Harga": 35000},
    {"Tanggal": "2025-07-03", "Warna": "Merah", "Ukuran": "S", "Jumlah": 4, "Harga": 20000},
    {"Tanggal": "2025-07-04", "Warna": "Putih", "Ukuran": "M", "Jumlah": 2, "Harga": 25000},
    {"Tanggal": "2025-07-04", "Warna": "Hitam", "Ukuran": "L", "Jumlah": 1, "Harga": 30000},
    {"Tanggal": "2025-07-05", "Warna": "Merah", "Ukuran": "XL", "Jumlah": 1, "Harga": 35000},
    {"Tanggal": "2025-07-05", "Warna": "Putih", "Ukuran": "S", "Jumlah": 3, "Harga": 20000},
    {"Tanggal": "2025-07-06", "Warna": "Hitam", "Ukuran": "M", "Jumlah": 2, "Harga": 25000},
    {"Tanggal": "2025-07-06", "Warna": "Merah", "Ukuran": "L", "Jumlah": 3, "Harga": 30000},
]

df = pd.DataFrame(data)
warna_order = ["Merah", "Putih", "Hitam"]
warna_terjual = df.groupby("Warna")["Jumlah"].sum().reindex(warna_order).fillna(0).astype(int)
total_kaos = warna_terjual.sum()
probabilitas = (warna_terjual / total_kaos) * 100

warna_grafik = ['red', 'white', 'black']

plt.figure(figsize=(8, 5))
plt.bar(probabilitas.index, probabilitas.values,
        color=warna_grafik, edgecolor='gray')

plt.title("Probabilitas Pembelian Kaos per Warna (6 Hari)")
plt.ylabel("Persentase (%)")
plt.xlabel("Warna")
plt.ylim(0, 50)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

warna_data = list(zip(warna_terjual.index, warna_terjual.values))

def bubble_sort(data):
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][1] < data[j + 1][1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data

sorted_data = bubble_sort(warna_data)

print("\nHasil Pengurutan (Bubble Sort) Berdasarkan Jumlah Terbanyak:")
for warna, jumlah in sorted_data:
    print(f"{warna}: {jumlah} kaos")

plt.figure(figsize=(8, 5))

sorted_warna, sorted_jumlah = zip(*sorted_data)

warna_grafik_sorted = [
    "red" if w == "Merah"
    else "white" if w == "Putih"
    else "black"
    for w in sorted_warna
]

plt.bar(sorted_warna, sorted_jumlah,
        color=warna_grafik_sorted, edgecolor="gray")

plt.title("Hasil Bubble Sort: Warna Kaos Paling Banyak Terjual")
plt.ylabel("Jumlah Kaos")
plt.xlabel("Warna")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# Simpan plot ke file
out_path = os.path.join(os.path.dirname(__file__), 'bubble_sort_result.png')
plt.gcf().savefig(out_path, dpi=150)
print(f'\nSaved sorted plot to: {out_path}')

plt.show()