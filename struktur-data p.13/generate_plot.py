import pandas as pd
import matplotlib.pyplot as plt
import os

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

out_path = os.path.join(os.path.dirname(__file__), 'penjualan_warna.png')

df = pd.DataFrame(data)
df['Total'] = df['Jumlah'] * df['Harga']
warna_order = ["Merah", "Putih", "Hitam"]
warna_terjual = df.groupby('Warna')['Jumlah'].sum().reindex(warna_order).fillna(0).astype(int)

colors_map = {"Merah": "red", "Putih": "lightgray", "Hitam": "black"}
bar_colors = [colors_map.get(w, 'tab:blue') for w in warna_terjual.index]
ax = warna_terjual.plot(kind='bar', color=bar_colors)
ax.set_ylabel('Jumlah Terjual')
ax.set_title('Penjualan per Warna (6 Hari)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.gcf().savefig(out_path, dpi=150)
print('Saved plot to:', out_path)
