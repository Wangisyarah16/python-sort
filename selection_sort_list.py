def selection_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

angka = [9, 5, 3, 8, 2]
selection_sort(angka)
print("Daftar angka setelah diurutkan:")
print(angka)