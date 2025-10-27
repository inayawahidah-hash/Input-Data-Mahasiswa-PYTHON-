def faktorial_dengan_penjelasan(n):
    # Faktorial dari 0 adalah 1
    if n == 0:
        print(f"{n}! = 1")
        return 1
    
    # Persiapan string untuk penjelasan
    penjelasan = f"{n}! = "
    for i in range(n, 0, -1):
        penjelasan += str(i)
        if i > 1:
            penjelasan += " x "
            
    # Inisialisasi hasil
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    
    # Menampilkan penjelasan dan hasil akhir
    print(penjelasan)
    print(f"Hasil dari {n}! adalah: {hasil}")
    return hasil

# --- Bagian Utama Program ---
try:
    angka = int(input("Masukkan sebuah bilangan bulat: "))
    
    if angka < 0:
        print("Faktorial tidak terdefinisi untuk bilangan negatif.")
    else:
        print("-" * 20) # Garis pemisah
        faktorial_dengan_penjelasan(angka)

except ValueError:
    print("Input tidak valid. Harap masukkan bilangan bulat.")