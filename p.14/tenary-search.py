def ternary_search(arr, key, low, high):
    if high >= low:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] == key:
            return mid1

        if arr[mid2] == key:
            return mid2

        if key < arr[mid1]:
            return ternary_search(arr, key, low, mid1 - 1)
        elif key > arr[mid2]:
            return ternary_search(arr, key, mid2 + 1, high)
        else:
            return ternary_search(arr, key, mid1 + 1, mid2 - 1)

    return -1


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Array saat ini:", data)

cari = int(input("Masukkan angka yang ingin dicari: "))

hasil = ternary_search(data, cari, 0, len(data) - 1)

if hasil != -1:
    print("Angka ditemukan di index:", hasil)
else:
    print("Angka tidak ditemukan dalam array.")