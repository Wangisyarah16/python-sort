def bubble_sort_books(buku):
    n = len(buku)

    for i in range(n):
        menukar = False
        for j in range(0, n - i - 1):
            if buku[j][2] > buku[j + 1][2]:
                buku[j], buku[j + 1] = buku[j + 1], buku[j]
                menukar = True
        if not menukar:
            break

buku = [
    ["Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 320],
    ["To Kill a Mockingbird", "Harper Lee", 281],
    ["The Great Gatsby", "F. Scott Fitzgerald", 180],
    ["Pride and Prejudice", "Jane Austen", 432],
    ["1984", "George Orwell", 328]
]

bubble_sort_books(buku)
print("Daftar buku setelah diurutkan berdasarkan jumlah halaman secara ascending:")
for i, book in enumerate(buku):
    print(f"No. {i+1}")
    print(f"Judul Buku: {book[0]}")
    print(f"Penulis: {book[1]}")
    print(f"Jumlah Halaman: {book[2]}")
    print()
