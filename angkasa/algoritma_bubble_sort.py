angka=[9,5,2,8,1]
for i in range(len(angka)):
    for j in range(0, len(angka)-i-1):
        if angka[j] > angka[j+1]:
            angka[j], angka[j+1] = angka[j+1], angka[j]
print("Hasil pengurutan dengan bubble sort:", angka)