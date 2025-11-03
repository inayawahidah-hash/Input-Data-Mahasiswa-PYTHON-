# Program Python untuk menyelesaikan tugas praktikum lesson 11

# --- TUGAS 1: Barisan Aritmetika ---
# Barisan: 2, 6, 10, 14, ...
# Ini adalah barisan aritmetika.
# Suku pertama (a) = 2
# Beda (b) = 6 - 2 = 4

class BarisanAritmetika:
    """
    Class ini merepresentasikan barisan aritmetika.
    Sesuai konsep OOP, class adalah 'template'[cite: 15].
    """
    
    def __init__(self, a, b):
        """
        Ini adalah constructor[cite: 31].
        Attributes-nya adalah suku pertama (a) dan beda (b)[cite: 28].
        """
        self.a = a  # Suku pertama
        self.b = b  # Beda
    
    def hitung_suku_ke_n(self, n):
        """
        Ini adalah method [cite: 38] untuk menghitung suku ke-n (Un).
        Rumus: Un = a + (n - 1) * b
        Kita menggunakan 'self' untuk mengakses attribute class[cite: 44, 45].
        """
        un = self.a + (n - 1) * self.b
        return un

# --- TUGAS 2: Luas Belah Ketupat ---
# Rumus: Luas = 1/2 * diagonal1 * diagonal2

class BelahKetupat:
    """
    Class ini merepresentasikan belah ketupat.
    """
    
    def __init__(self, d1, d2):
        """
        Constructor untuk menyimpan attribute [cite: 28] diagonal 1 (d1) 
        dan diagonal 2 (d2).
        """
        self.d1 = d1
        self.d2 = d2
        
    def hitung_luas(self):
        """
        Method [cite: 38] untuk menghitung luas belah ketupat.
        Rumus: L = 0.5 * d1 * d2
        """
        luas = 0.5 * self.d1 * self.d2
        return luas

# --- EKSEKUSI PROGRAM ---

print("--- Hasil Tugas 1: Suku ke-98 ---")
# Membuat object [cite: 46] dari class BarisanAritmetika
# a = 2, b = 4
barisan_soal = BarisanAritmetika(a=2, b=4)

# Menentukan suku ke-98 
n_dicari = 98
hasil_suku_98 = barisan_soal.hitung_suku_ke_n(n_dicari)

print(f"Barisan: 2, 6, 10, 14, ...")
print(f"Suku pertama (a): {barisan_soal.a}")
print(f"Beda (b): {barisan_soal.b}")
print(f"Suku ke-{n_dicari} (U{n_dicari}) adalah: {hasil_suku_98}")


print("\n--- Hasil Tugas 2: Luas Belah Ketupat ---")
# Membuat object [cite: 46] dari class BelahKetupat
# Kita gunakan contoh d1 = 20 dan d2 = 30
d1_contoh = 20
d2_contoh = 30
belah_ketupat_1 = BelahKetupat(d1=d1_contoh, d2=d2_contoh)

# Memanggil method [cite: 38] hitung_luas()
luas = belah_ketupat_1.hitung_luas()

print(f"Belah ketupat dengan:")
print(f"Diagonal 1 (d1): {belah_ketupat_1.d1}")
print(f"Diagonal 2 (d2): {belah_ketupat_1.d2}")
print(f"Luasnya adalah: {luas}")