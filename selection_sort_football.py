def selection_sort_players(pemain):
    n = len(pemain)

    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if pemain[j][2] > pemain[max_idx][2]:
                max_idx = j
        pemain[i], pemain[max_idx] = pemain[max_idx], pemain[i]

pemain = [
    ["Kylian Mbappe", "Paris Saint Germain", 40],
    ["Victor Osimhen", "Napoli", 28],
    ["Robert Lewandowski", "Barcelona", 33],
    ["Erling Haaland", "", 52],
    ["Christopher Nkunku", "RB Leipzig", 22]
]

selection_sort_players(pemain)
print("Daftar pemain setelah diurutkan berdasarkan jumlah gol secara descending:")
for i, player in enumerate(pemain):
    print(f"No. {i+1}")
    print(f"Nama Pemain: {pemain[0]}")
    print(f"Klub: {pemain[1]}")
    print(f"Jumlah Gol: {pemain[2]}")
    print()
