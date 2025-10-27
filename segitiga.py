# Minta input dari user
x = int(input("Masukkan angka :"))

# Siapkan variabel string kosong
string = ""

# Lebar maksimum diperlukan agar bisa dicetak di tengah.
# Baris terlebar punya (2*x-1) bintang.
# Untuk input 5, ada 9 bintang, lebar karakternya 17 ('* * * * * * * * *')
lebar_maks = (x * 2 - 1) * 2

# ======================================================
# BAGIAN ATAS (Dari 9 bintang sampai 1 bintang di tengah)
# ======================================================
bar = x
while bar >= 1:
    # Jumlah bintang menurun ganjil: 9, 7, 5, 3, 1
    jumlah_bintang = (bar * 2) - 1
    
    # Membuat baris bintang, contoh: '* * * * *'
    baris_bintang = ' '.join(['*'] * jumlah_bintang)
    
    # Menambahkan baris yang sudah dipusatkan ke string utama
    string = string + baris_bintang.center(lebar_maks) + "\n"
    
    bar = bar - 1

# ======================================================
# BAGIAN BAWAH (Dari 3 bintang sampai 9 bintang lagi)
# ======================================================
bar = 2
while bar <= x:
    # Jumlah bintang menaik ganjil: 3, 5, 7, 9
    jumlah_bintang = (bar * 2) - 1

    # Membuat baris bintang
    baris_bintang = ' '.join(['*'] * jumlah_bintang)

    # Menambahkan baris yang sudah dipusatkan ke string utama
    string = string + baris_bintang.center(lebar_maks) + "\n"

    bar = bar + 1

# Cetak hasil akhir yang sudah terkumpul di variabel string
print(string)