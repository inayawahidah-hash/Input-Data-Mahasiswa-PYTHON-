#input data
data_mahasiswa = []
jumlah_mahasiswa = int(input("Input jumlah mahasiswa: "))
for i in range(jumlah_mahasiswa):
    print(f"\nMahasiswa {i + 1}")
    nama   = input("Nama : ")
    umur   = input("Umur : ")
    alamat = input("Alamat: ")
    
    data_mahasiswa.append([nama,umur,alamat])
    print("\n=== Data Mahasiswa ===")
    for i in range (len(data_mahasiswa)):
        print(f"Mahasiswa {i+1}") 
        print("Nama : ",data_mahasiswa[i][0])
        print("Umur : ",data_mahasiswa[i][1])
        print("Alamat : ",data_mahasiswa[i][2])
    