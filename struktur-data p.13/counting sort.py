def counting_sort(arr):
    print("input array:", arr)
    if not arr:
        print("Output (terurut): []")
        return []
    if min(arr) < 0:
        raise ValueError("counting_sort only supports non-negative integers")
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    print("frekuensi (count array):")
    for i, c in enumerate(count):
        if c > 0:
            print(f"Angka {i}: {c} kali")

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    print("Output (terurut):", sorted_arr)
    return sorted_arr

data = [4, 2, 2, 8, 3, 3, 1]
counting_sort(data)