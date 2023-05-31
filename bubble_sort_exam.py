def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        menukar = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                menukar = True
        if not menukar:
            break

nilai = [78, 65, 90, 82, 70]
bubble_sort(nilai)
print("Daftar nilai setelah diurutkan:")
print(nilai)
