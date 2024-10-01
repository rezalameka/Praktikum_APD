username_anda = "reza"
password_anda = 107
count = 1

while count < 4:
    username = str(input("Masukkan username anda: "))
    password = int(input("Masukkan password anda: "))
    
    if (username == username_anda) and (password == password_anda):
        print("Login Berhasil")
    menu = int(input("Masukan Pilihan 1/2:"))
    if menu == 1:
        mobil_merk = str(input("Masukkan merk mobil:"))
        harga_mobil = float(input("Masukkan harga mobil:"))

        if mobil_merk == "tesla":
             bayar_tesla = (harga_mobil -(harga_mobil*0.17))
             print("Harga yang harus dibayar = RP.",bayar_tesla)
        elif mobil_merk == "toyota":
            bayar_toyota = (harga_mobil-(harga_mobil*0.21))
            print("Harga yang harus di bayar = RP.",bayar_toyota)
        elif mobil_merk == "hyundai":
            bayar_hyundai = (harga_mobil-(harga_mobil*0.23))
            print(f"Harga yang harus dibayar = RP.{bayar_hyundai:,.0f}")
        else:
            print("tidak jadi membeli mobil")
            break
    elif menu == 2:
                print("Anda memilih untuk keluar.")
                break   
    else:
        count += 1
        print(f"Username atau Password salah,Anda Memiliki {4-count} Kesempatan Lagi")