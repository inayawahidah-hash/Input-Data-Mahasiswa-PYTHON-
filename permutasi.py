def faktorial(n):
    """Fungsi faktorial sederhana tanpa print, untuk perhitungan internal."""
    if n == 0:
        return 1
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

def permutasi_dengan_penjelasan(n, r):
    """Fungsi untuk menghitung permutasi dan memberikan penjelasan."""
    if n < r:
        print(f"Error: nilai n ({n}) tidak boleh lebih kecil dari r ({r}).")
        return
        
    # Menampilkan rumus yang digunakan
    print(f"Menghitung P({n}, {r}) menggunakan rumus: n! / (n - r)!")
    print(f"P({n}, {r}) = {n}! / ({n} - {r})!")
    
    # Menghitung nilai-nilai yang dibutuhkan
    n_faktorial = faktorial(n)
    n_minus_r = n - r
    n_minus_r_faktorial = faktorial(n_minus_r)
    
    # Menampilkan hasil perhitungan faktorial
    print(f"P({n}, {r}) = {n_faktorial} / {n_minus_r}!")
    print(f"P({n}, {r}) = {n_faktorial} / {n_minus_r_faktorial}")
    
    # Menghitung dan menampilkan hasil akhir
    hasil_akhir = n_faktorial // n_minus_r_faktorial
    print(f"Hasil akhir P({n}, {r}) adalah: {hasil_akhir}")

# --- Bagian Utama Program ---
try:
    n = int(input("Masukkan nilai n: "))
    r = int(input("Masukkan nilai r: "))
    print("-" * 20) # Garis pemisah
    permutasi_dengan_penjelasan(n, r)

except ValueError:
    print("Input tidak valid. Harap masukkan bilangan bulat.")