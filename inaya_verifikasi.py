data = input("Masukkan Umur Kamu: ").strip()

if not data:
    print("❌ Input tidak boleh kosong!")
else:
    try:
        angka = int(data)
        print(f"✅ Data ini adalah angka integer. Angka = {angka}")
    except ValueError:
        try:
            angka = float(data)
            print(f"✅ Data ini adalah data float. Angka = {angka}")
        except ValueError:
            print(f"ℹ️ Data yang anda inputkan adalah tipe string ({type(data).__name__})")
