def nilai_ke_bobot(nilai): 
    konversi = {
        "A": 4.0,
        "B+": 3.5,
        "B": 3.0,
        "C+": 2.5,
        "D": 1.0,
        "E": 0.0
    }
    return konversi.get(nilai.upper(), 0)

#INPUT DATA DIRI
print("===== INPUT IDENTITAS MAHASISWA =====")
nama = input ("nama mahasiswa : ")
npm = input ("npm             : ")

#INPUT JUMLAH MATA KULIAH
jml = int(input("\nMasukkan jumlah mata kuliah: "))

matkul_list = []
total_sks = 0
total_nxb = 0

#INPUT DATA PER-MATA KULIAH
for i in range (jml):
    print(f"\n--- Mata kuliah ke-{i+1} ---")
    matkul = input("nama mata kuliah : ")
    sks = int(input("jumlah sks      : "))
    nilai = input("nilai (A/B+/B/B/C+/C/D/E)  : ")

    bobot = nilai_ke_bobot(nilai)
    nxk = sks * bobot

    matkul_list.append([matkul, sks, nilai, bobot, nxk])
    total_sks  += sks
    total_nxb  += nxk

#HITUNG IP
ip = total_nxb / total_sks if total_sks else 0

#OUTPUT KHS
print("\n============KHS MAHASISWA=============")
print(f"nama  :{nama}")
print(f"npm   :{npm}")
print("----------------------------------------")
print("{:<25}  {:<5}  {:<6}  {:<6}  {:<6} ".format ("mata kuliah",  "sks",  "nilai",  "bobot",  "nxb"))

for m in matkul_list:
    print("{:<25}  {:<5}  {:<6}  {:<6}  {:<6} ".format(m[0], m[1], m[2], m[3], m[4]))

print("---------------------------------------------------------------------")
print(f"total sks : {total_sks}")
print(f"total nxb : {total_nxb}")
print(f"ip semester : {ip:.2f}")
print("======================================================================")



# =======================================================================
# TAMBAHAN FITUR SESUAI FLOWCHART (TANPA MERUBAH CODINGAN ASLI)
# =======================================================================

import os

filename = "khs_mahasiswa.txt"

# 1. CEK APAKAH FILE TXT ADA
if not os.path.exists(filename):
    print("\nFile TXT belum ada, membuat file baru...")
    with open(filename, "w") as f:
        f.write("=== DATA KHS MAHASISWA ===\n\n")

# 2. TULIS DATA KHS KE DALAM FILE TXT
with open(filename, "a") as f:
    f.write(f"Nama : {nama}\n")
    f.write(f"NPM  : {npm}\n")
    f.write("----------------------------------------\n")
    f.write("{:<25} {:<5} {:<6} {:<6} {:<6}\n".format("Mata Kuliah", "SKS", "Nilai", "Bobot", "NXB"))

    for m in matkul_list:
        f.write("{:<25} {:<5} {:<6} {:<6} {:<6}\n".format(m[0], m[1], m[2], m[3], m[4]))

    f.write("----------------------------------------\n")
    f.write(f"Total SKS : {total_sks}\n")
    f.write(f"Total NXB : {total_nxb}\n")
    f.write(f"IP Semester : {ip:.2f}\n")
    f.write("========================================\n\n")

print("\nData berhasil disimpan ke file TXT!")
