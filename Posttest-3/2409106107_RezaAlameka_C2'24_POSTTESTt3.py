mobil_merk = str(input("Masukkan merk mobil:"))
harga_mobil = float(input("Masukkan harga mobil:"))
#proses
if mobil_merk == "tesla":
    bayar_tesla = (harga_mobil -(harga_mobil*0.17))
    print("Harga yang harus dibayar = RP.",bayar_tesla)
elif mobil_merk == "toyota":
    bayar_toyota = (harga_mobil-(harga_mobil*0.21))
    print("Harga yang harus di bayar = RP.",bayar_toyota)
elif mobil_merk == "hyundai":
    bayar_hyundai = (harga_mobil-(harga_mobil*0.23))
    print("Harga yang harus dibayar = RP.",bayar_hyundai)
else :
    print("tidak jadi membeli mobil")