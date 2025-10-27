def input_data():
    print("\n=== Input Data Siswa ===")
    nama = input("Masukkan nama siswa: ")
    print(f"Data '{nama}' berhasil ditambahkan!\n")


def tampilkan_data():
    print("\n=== Tampilkan Data Siswa ===")
    print("Belum ada data.\n")


while True:
    print("\nMenu Aplikasi Data Siswa Linkedlist Python")
    print("-------------------------------------------")
    print("1. Input Data Siswa")
    print("2. Tampilkan Data Siswa")
    print("3. Update Data Siswa")
    print("4. Hapus Data Siswa")
    print("5. Author")
    print("6. Keluar Aplikasi")

    pilih = input("Masukkan Pilihan Anda: ")

    if pilih == "1":
        input_data()
    elif pilih == "2":
        tampilkan_data()
    elif pilih == "3":
        print("Fitur update data belum tersedia.\n")
    elif pilih == "4":
        print("Fitur hapus data belum tersedia.\n")
    elif pilih == "5":
        print("\nAuthor: Inaya Nur Wahidah\n")
    elif pilih == "6":
        print("Terima kasih, program selesai.")
        break
    else:
        print("Pilihan tidak valid, coba lagi ya.\n")
