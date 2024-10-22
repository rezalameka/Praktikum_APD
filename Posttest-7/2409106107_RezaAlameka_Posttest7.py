# Variabel global
gudang = {
    "Kabel": {'tipe': 'NYA', 'stok': 500},
    "Lampu": {'tipe': '5 Watt', 'stok': 200},
    "Kunci": {'tipe': 'satu set L', 'stok': 30},
    "Laptop": {'tipe': "Acer", 'stok': 90}
}

pengguna = {
    "admin": {'password': 'admin', 'peran': 'admin'},
    "pengguna": {'password': 'pengguna', 'peran': 'pengguna'}
}

# Fungsi untuk menampilkan inventaris
def tampilkan_inventaris():
    print("\n==== Daftar Alat ====")
    for alat, detail in gudang.items():
        print(f"Nama Alat: {alat}, Tipe Alat: {detail['tipe']}, Stok Alat: {detail['stok']}")

# Fungsi untuk menambahkan alat baru
def tambah_alat(nama_alat, tipe_alat, stok_alat):
    gudang[nama_alat] = {'tipe': tipe_alat, 'stok': stok_alat}
    print(f"Alat '{nama_alat}' berhasil ditambahkan!")

# Fungsi untuk memperbarui alat
def perbarui_alat(nama_alat):
    if nama_alat in gudang:
        tipe_alat = input("Masukkan tipe alat baru: ")
        try:
            stok_alat = int(input("Masukkan stok alat baru: "))
            gudang[nama_alat] = {'tipe': tipe_alat, 'stok': stok_alat}
            print(f"Alat '{nama_alat}' berhasil diperbarui!")
        except ValueError:
            print("Input stok tidak valid. Harap masukkan angka.")
    else:
        print("Alat tidak ditemukan!")

# Prosedur untuk registrasi pengguna
def registrasi_pengguna():
    print("\n==== Registrasi ====")
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")
    peran = input("Masukkan peran (admin/pengguna): ")

    if username not in pengguna:
        pengguna[username] = {'password': password, 'peran': peran}
        print("Akun berhasil didaftarkan!")
    else:
        print("Username sudah terpakai!")

# Prosedur untuk login pengguna
def login_pengguna():
    print("\n==== Login ====")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in pengguna and pengguna[username]['password'] == password:
        print("Login berhasil!")
        return pengguna[username]
    else:
        print("Username atau password salah.")
        return None

# Loop utama program
while True:
    print("""
  Selamat Datang di E-GUDANG ELEKTRONIK
==========================================
               1. Registrasi             
               2. Login                  
               3. Exit                   
==========================================

""")
    try:
        pilihan = int(input("Pilih opsi: "))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        continue

    if pilihan == 1:
        registrasi_pengguna()

    elif pilihan == 2:
        akun_masuk = login_pengguna()
        if akun_masuk:
            if akun_masuk['peran'] == 'admin':
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
                    try:
                        kuasa_admin = int(input("Pilih opsi: "))
                    except ValueError:
                        print("Input tidak valid. Harap masukkan angka.")
                        continue

                    if kuasa_admin == 1:
                        nama_alat = input("Masukkan nama alat: ")
                        tipe_alat = input("Masukkan tipe alat: ")
                        try:
                            stok_alat = int(input("Masukkan stok alat: "))
                            tambah_alat(nama_alat, tipe_alat, stok_alat)
                        except ValueError:
                            print("Input stok tidak valid. Harap masukkan angka.")

                    elif kuasa_admin == 2:
                        tampilkan_inventaris()

                    elif kuasa_admin == 3:
                        nama_alat = input("Masukkan nama alat yang ingin diperbarui: ")
                        perbarui_alat(nama_alat)

                    elif kuasa_admin == 4:
                        nama_alat = input("Masukkan nama alat yang ingin dihapus: ")
                        if nama_alat in gudang:
                            del gudang[nama_alat]
                            print("Alat berhasil dihapus!")
                        else:
                            print("Alat tidak ditemukan!")

                    elif kuasa_admin == 5:
                        print("Logout berhasil.")
                        break
                    else:
                        print("Pilihan tidak valid.")

            elif akun_masuk['peran'] == 'pengguna':
                while True:
                    print("""
    ======================================================================
    =                          Menu Pengguna                             =
==============================================================================
    =                          1. Lihat Alat                             =             
    =                          4. Log Out                                =               
    ======================================================================

""")
                    try:
                        pengguna_aja = int(input("Pilih opsi: "))
                    except ValueError:
                        print("Input tidak valid. Harap masukkan angka.")
                        continue

                    if pengguna_aja == 1:
                        tampilkan_inventaris()

                    elif pengguna_aja == 4:
                        print("Logout berhasil.")
                        break
                    else:
                        print("Silahkan pilih nomor yang tertera!!!.")

    elif pilihan == 3:
        print("Terima kasih telah E-GUDANG ini.")
        break

    else:
        print("Silahkan pilih nomor yang tertera!!!.")