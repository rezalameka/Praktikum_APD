# ISI GUDANG
gudang = [["Kabel", "NYA", 500], ["Lampu", "5 Watt", 200], ["Kunci", "satu set L", 30]]

# Langsung Login ADMIN 
users = [["admin", "aslabgacor", "admin"]]



while True:
    
        print("""
        Selamat Datang di E-GUDANG
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
            role = input("Masukkan peran (admin/pengguna): ").lower()

            if role not in ["admin", "pengguna"]:
                raise ValueError("Peran tidak valid. Pilih 'admin' atau 'pengguna'.")

            users.append([username, password, role])
            print(f"Registrasi berhasil untuk {username} sebagai {role}.\n")

        elif pilih == 2:
            print("\n==== Login ====")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            for user in users:
                if user[0] == username and user[1] == password:
                    akun_masuk = user
                    print(f"Login berhasil! Selamat datang, {akun_masuk[0]}.\n")
                    continue
            else:
                     print("Username atau password salah.")

            if akun_masuk[2] == "admin":
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
                        print("\n==== Tambah Alat ====")
                        nama_alat = input("Masukkan Nama alat: ")
                        tipe_alat = (input("Masukkan Tipe alat: "))
                        stock_alat = (input("Masukkan Stock alat: "))
                        gudang.append([nama_alat, tipe_alat, stock_alat])
                        print(f"Alat '{nama_alat}' berhasil ditambahkan.")

                    elif kuasa_admin == 2:
                        print("\n==== Daftar Alat ====")
                        for item in gudang:
                            print(f"Nama Alat: {item[0]}, Tipe alat: {item[1]}, Stock alat: {item[2]}")

                    elif kuasa_admin == 3:
                        print("\n==== Update Alat ====")
                        nama_alat = input("Masukkan nama alat yang ingin diupdate: ")
                        for item in gudang:
                            if item[0] == nama_alat:
                                item[1] = (input(f"Masukkan tipe baru untuk alat {nama_alat}: "))
                                item[2] = (input(f"Masukkan stock baru untuk alat {nama_alat}: "))
                                print(f"Alat '{nama_alat}' berhasil diupdate.")
                                break
                        else:
                            print(f"Alat '{nama_alat}' tidak ditemukan.")

                    elif kuasa_admin == 4:
                        print("\n==== Hapus Alat ====")
                        nama_alat = input("Masukkan nama alat yang ingin dihapus: ")
                        for item in gudang:
                            if item[0] == nama_alat:
                                gudang.remove(item)
                                print(f"Alat '{nama_alat}' berhasil dihapus.")
                                break
                        else:
                            print(f"Alat '{nama_alat}' tidak ditemukan.")

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
                        for item in gudang:
                            print(f"Nama Alat: {item[0]}, Tipe alat: {item[1]}, Stock alat: {item[2]}")
                        

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
