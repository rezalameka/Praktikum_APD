nama =input("Masukkan Nama: ")
nim =input("Masukkan NIM: ")
harga_mobil_tesla =int(input("Masukkan Harga Mobil tesla: RP." ))
diskon_tesla = harga_mobil_tesla - (0.17*harga_mobil_tesla)
harga_mobil_toyota =int(input("Masukkan Harga Mobil toyota: RP."))
diskon_toyota = harga_mobil_toyota - (0.21*harga_mobil_toyota)
harga_mobil_hyundai =int(input("Masukkan Harga Mobil hyundai: RP."))
diskon_hyundai = harga_mobil_hyundai - (0.23*harga_mobil_hyundai)
mod_tesla = harga_mobil_tesla % 7
mod_toyota = harga_mobil_toyota % 7
mod_hyundai = harga_mobil_hyundai % 7
#deklarasi var
nama =str(nama)
nim = int(nim)
harga_mobil_tesla =int(harga_mobil_tesla)
harga_mobil_toyota =int(harga_mobil_toyota)
harga_mobil_hyundai =int(harga_mobil_hyundai)
diskon_tesla =int(diskon_tesla)
diskon_toyota =int(diskon_toyota)
diskon_hyundai =int(diskon_hyundai)
mod_tesla =int(mod_tesla)
mod_toyota =int(mod_toyota)
mod_hyundai = int(mod_hyundai)
print("------------------------------------------------")
print("Nama Anda Adalah", nama)
print("NIM Anda Adalah", nim)
print("------------------------------------------------")
print("MENGHITUNG HARGA DISKON MOBIL")
print(f"Mobil tesla seharga RP. {harga_mobil_tesla}"
      f" diskon 17 % menjadi RP. {diskon_tesla}")
print(f"Mobil toyota seharga RP. {harga_mobil_toyota}"
      f" diskon 21 % menjadi RP. {diskon_toyota}")
print(f"Mobil hyundai seharga RP. {harga_mobil_hyundai}"
      f" diskon 23 % menjadi RP. {diskon_hyundai}")
print("------------------------------------------------")
print("MENAMPILKAN HASIL MODULUS 7 DARI HARGA SETIAP MOBIL")
print("Modulus Tesla = ", mod_tesla)
print("Modulus Toyota = ", mod_toyota)
print("Modulus Hyundai = ", mod_hyundai)