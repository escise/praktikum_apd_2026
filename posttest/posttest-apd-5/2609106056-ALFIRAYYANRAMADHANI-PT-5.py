import os

user_pw_admin = ("alfi", "2008")
user_pw = ()

reg = False
log = False
admin_privilege = False

percobaan = 0

list_br_elektronik = [
    ["Laptop Ideapad", "Legowo", "Rp.10000000", 5],
    ["Iphonk 67", "Apel", "Rp.99000000", 2],
    ["Tab Samsul", "Samsul", "Rp.10000000", 1],
]

os.system("cls")

while True:
    print("Pilih Metode Login anda")
    print("1. Register")
    print("2. Login")
    print("3. Keluar dari sistem")
    rgs = input("Pilih Opsi: ")
    
    if rgs.isdigit():
        rgs = int(rgs)
        if rgs == 1:
            reg = True
            break
        elif rgs == 2:
            log = True
            os.system("cls")
            break
        elif rgs == 3:
            exit()
        else:
            os.system("cls")
            print("angka invalid")
    else:
        os.system("cls")
        print("Input harus berupa angka")

while reg:
    rgs_user = input("masukkan user registrasi baru anda: ")
    rgs_pass = input("masukkan password registrasi baru anda: ")

    if rgs_pass.isdigit():
        if rgs_user in user_pw:
            print("Username tidak boleh sama")
        else:
            user_pw = user_pw + ([rgs_user, rgs_pass],)
            os.system("cls")

            rgs_cb = input("Apakah anda ingin login atau registrasi akun baru lagi? (ya/tidak): ").strip().lower()

            if rgs_cb in ["y", "ya", "iya", "yes", 1]:
                print("silahkan isi akun baru lagi.")
            elif rgs_cb in ["n", "tidak", "tak", "no", "t", 0]:
                print("silahkan login.")
                log = True
                print(user_pw)
                break
    else:
        os.system("cls")
        print("password yang akan digunakan harus berupa angka.")

while percobaan < 3 and log:
    log_user = input("Masukkan username anda: ").strip().lower()
    log_pw = input("Masukkan password anda: ")
    print([log_user, log_pw])
    if log_user == user_pw_admin[0] and log_pw == user_pw_admin[1]:
        os.system("cls")
        admin_privilege = True
        break
    elif [log_user, log_pw] in user_pw:
        os.system("cls")
        break
    else:
        print("user atau password invalid")
        percobaan += 1
    if percobaan == 3:
        print("anda gagal login sebanyak tiga kali")

# Create, Read, Update, dan Delete sesuai dengan privilege-nya masing-masing
while True:
    print('''
        =============== Selamat Datang ================
        
        1. Buka List Stok Barang Elektronik
        2. Tambah Stok Barang Elektronik Baru (Admin)
        3. Update Stok Barang Elektronik (Admin)
        4. Hapus Stok Barang Elektronik (Admin)
        5. Keluar dari Program
        
        ===============================================
    ''')
    
    opsi_in_menu = input("Masukkan Opsi Anda (1-4): ")

    if not opsi_in_menu.isdigit() or not opsi_in_menu:
        print("Input Harus berupa angka atau tidak boleh kosong.")
    else:
        opsi_in_menu = int(opsi_in_menu)
        # read part
        if opsi_in_menu == 1:
            os.system("cls")
            print("list barang elektronik")
            for a, b, c, d in list_br_elektronik:
                print(f'''
                Nama Barang : {a}
                Nama Brand  : {b}
                Harga Barang: {c}
                Sisa Stok   : {d}
                ''')
            back = input("Back?: ").strip().lower()
            os.system("cls")
        # create part
        elif opsi_in_menu == 2:
            if admin_privilege:
                os.system("cls")
                konfirmasi = input("Apakah Anda ingin menambahkan Barang Elektronik Baru? (y/n): ").lower().strip()

                if konfirmasi == "y":
                    while True:
                        nm_br_baru = input("Nama Barang Baru: ").strip()
                        mrk_br_baru = input("Nama Merek/Brand: ").strip()
                        hrg_br_baru = input("Harga Barang Baru: ").strip()
                        st_br_baru = input("Berapa stok?: ")

                        # i dont know this shit man
                        if not (st_br_baru.isdigit() and nm_br_baru and mrk_br_baru and hrg_br_baru.isdigit()):
                            os.system("cls")
                            print("Salah satu atau lebih masukkan tidak valid")
                        else:
                            list_br_elektronik = list_br_elektronik + [[nm_br_baru, mrk_br_baru, f"Rp.{hrg_br_baru}", st_br_baru],]
                            dua_lagi = input("Apakah Anda ingin menambahkan Barang Elektronik Baru lagi? (y/n): ").strip().lower()
                            
                            if dua_lagi == "y":
                                os.system("cls")
                            else:
                                os.system("cls")
                                print("masukkan di terima.")
                                break
                else:       
                    pass
            else:
                print("Anda bukan seorang admin")
        elif opsi_in_menu == 3:
            if admin_privilege:
                os.system("cls")
                konfirmasi = input("Apakah Anda ingin menambahkan Barang Elektronik Baru? (y/n): ").lower().strip()
                
                if konfirmasi == "y":
                    while True:
                        upd_in = input("")
            else:
                print("Anda bukan seorang admin")
        elif opsi_in_menu == 4:
            if admin_privilege:
                print()
            else:
                print("Anda bukan seorang admin")
        elif opsi_in_menu == 5:
            exit()
        else:
            print("angka tidak ada dalam jangkauan")    