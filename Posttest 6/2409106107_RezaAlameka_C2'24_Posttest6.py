gudang = {
    "Kabel": {'tipe': 'NYA', 'stock': 500},
    "Lampu": {'tipe': '5 Watt', 'stock': 200},
    "Kunci": {'tipe': 'satu set L', 'stock': 30},
    "Laptop" : {'tipe': "Acer", 'stock': 90}
}

# Initialize user data
users = {
    "admin": {'password': 'admin', 'role': 'admin'},
    "pengguna": {'password': 'pengguna', 'role': 'pengguna'}
}


while True:
    
        print("""
  Selamat Datang di E-GUDANG ELEKTRONIK
==========================================
               1. Registrasi             
               2. Login                  
               3. Exit                   
==========================================

""")
        pilih = int(input("Pilih opsi: "))

        if pilih == 1:
            print("\n==== Registrasi ====")
            username = input("Masukkan username baru: ")
            password = input("Masukkan password baru: ")
            role = input("Masukkan peran (admin/pengguna): ")

            if username not in users:
                users[username] = {'password': password, 'role': role}
                print("Akun berhasil didaftarkan!")
            else:
                print("Username sudah terpakai!")

        elif pilih == 2:
            print("\n==== Login ====")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            if username in users and users[username]['password'] == password:
                print("Login berhasil!")

            else:
                print("Username atau password salah.")

            if users[username]['role'] == 'admin':
                while True:
                    print("""
        ==============================================================
                                Khusus ADMIN             
   =========================================================================
   =                           1. Tambah Alat                             =
    =                          2. Lihat Alat                             =
     =                         3. Update Alat                           =
      =                        4. Hapus Alat                           =
       =                       5. Log Out                             =
        ==============================================================

                          

""")
                    kuasa_admin = int(input("Pilih opsi: "))

                    if kuasa_admin == 1:
                        nama_alat = input("Masukkan nama alat: ")
                        tipe_alat = input("Masukkan tipe alat: ")
                        stock_alat = int(input("Masukkan stock alat: "))
                        gudang[nama_alat] = {'tipe': tipe_alat, 'stock': stock_alat}
                        print("Alat berhasil ditambahkan!")

                    elif kuasa_admin == 2:
                        print("\n==== Daftar Alat ====")
                        for alat, detail in gudang.items():
                            print(f"Nama Alat: {alat}, Tipe Alat: {detail['tipe']}, Stock Alat: {detail['stock']}")

                    elif kuasa_admin == 3:
                        print("\n==== Update Alat ====")
                        nama_alat = input("Masukkan nama alat yang ingin diupdate: ")
                        if nama_alat in gudang:
                            tipe_alat = input("Masukkan tipe alat baru: ")
                            stock_alat = int(input("Masukkan stock alat baru: "))
                            gudang[nama_alat] = {'tipe': tipe_alat, 'stock': stock_alat}
                            print("Alat berhasil diupdate!")
                        else:
                            print("Alat tidak ditemukan!")
                       

                    elif kuasa_admin == 4:
                        print("\n==== Hapus Alat ====")
                        nama_alat = input("Masukkan nama alat yang ingin dihapus: ")
                        if nama_alat in gudang:
                            del gudang[nama_alat]
                            print("Alat berhasil dihapus!")
                        else:
                            print("Alat tidak ditemukan!")

                    elif kuasa_admin == 5:
                        print("Logout berhasil.")
                        akun_masuk = None
                        break
                    else:
                        print("Pilihan tidak valid.")

            elif akun_masuk[2] == "pengguna":
                while True:
                    print("""
    ======================================================================
    =                          Menu Pengguna                             =
==============================================================================
    =                          1. Lihat Alat                             =             
    =                          4. Log Out                                =               
    ======================================================================

""")
                    pengguna_aja = int(input("Pilih opsi: "))

                    if pengguna_aja == 1:
                        print("\n==== Daftar Alat ====")
                        for alat, detail in gudang.items():
                            print(f"Nama Alat: {alat}, Tipe Alat: {detail['tipe']}, Stock Alat: {detail['stock']}")

                        

                    elif pengguna_aja == 4:
                        print("Logout berhasil.")
                        akun_masuk = None
                        break
                    else:
                        print("Silahkan pilih nomor yang tertera!!!.")

        elif pilih == 3:
            print("Terima kasih telah E-GUDANG ini.")
            break

        else:
            print("Silahkan pilih nomor yang tertera!!!.")
