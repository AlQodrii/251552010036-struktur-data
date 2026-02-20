angka=[3,7,2,9,1]
nilai_maksimum=angka[0]
for i in range(1,len(angka)):
    if angka[i]>nilai_maksimum:
        nilai_maksimum=angka[i]
print("Nilai maksimum dalam list adalah:",nilai_maksimum)