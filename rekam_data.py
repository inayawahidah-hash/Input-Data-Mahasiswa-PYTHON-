# Rekam Data Mahasiswa
# File : rekam_data.py

import sys
import os

class Mahasiswa:
    nim = ''
    nama = ''

pilih = 0
dataSiswa = []

def menu():
    os.system('cls')
    print("Menu Aplikasi Data Siswa LinkedList python")
    print("-------------------------------------------")
    print("1. Input Data Siswa")
    print("2. Tampilkan Data Siswa")
    print("3. Update Data Siswa")
    print("4. Hapus Data Siswa")
    print("5. Author")
    print("6. Keluar Aplikasi")
    pilih = int(input("Masukkan pilihan anda : "))
    if pilih == 1:
        pilih1()
        menu()
    elif pilih == 2:
        tampil()
        input("Kembali menu utama")
        menu()
    elif pilih == 3:
        index_update = -1
        tampil()
        id_edit = int(input("Input Nim yang akan di update : "))
        for a in range(0, len(dataSiswa)):
            if id_edit == dataSiswa[a].nim:
                index_update = a
                break
        if index_update > -1:
            print("INPUT DATA YANG DI UPDATE")
            siswa = Mahasiswa()
            siswa.nim = int(input("Masukkan nim : "))
            siswa.nama = input("Masukkan nama siswa : ")
            dataSiswa[index_update] = siswa
            print("Berhasil update data siswa")
        else:
            print("Nim tidak ditemukan")
        input("Kembali menu utama")
        menu()
    elif pilih == 4:
        os.system('cls')
        tampil()
        index_delete = -1
        id_hapus = int(input("Input Nim yang akan di hapus : "))
        for a in range(0, len(dataSiswa)):
            if id_hapus == dataSiswa[a].nim:
                index_delete = a
                break
        if index_delete > -1:
            del dataSiswa[index_delete]
            print("Data telah dihapus")
        else:
            print("Nim tidak ditemukan")
        input("Kembali menu utama")
        menu()
    elif pilih == 5:
        author()
        input("\n\nKembali menu utama")
        menu()
    elif pilih == 6:
        sys.exit()

def tampil():
    os.system('cls')
    print("DATA MAHASISWA")
    for data in dataSiswa:
        print("Nim   : " + str(data.nim))
        print("Nama  : " + data.nama)
        print("-----------------------------")

def author():
    os.system('cls')
    print("Alvin Meko | 672010193")
    print("UKSW 2015")

def pilih1():
    ulang = 'Y'
    while ulang in ('y', 'Y'):
        os.system('cls')
        siswaBaru = Mahasiswa()
        print("INPUT DATA MAHASISWA")
        siswaBaru.nim = int(input("Masukkan nim : "))
        siswaBaru.nama = input("Masukkan nama siswa : ")
        dataSiswa.append(siswaBaru)
        ulang = input("Apakah Anda Ingin Mengulang (Y/T)? ")

menu()
