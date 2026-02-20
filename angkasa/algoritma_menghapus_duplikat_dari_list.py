data=[1,2,3,2,4,1,5]
hasil=[]
for item in data:
    if item not in hasil:
        hasil.append(item)
print("List tanpa duplikat:",hasil)
