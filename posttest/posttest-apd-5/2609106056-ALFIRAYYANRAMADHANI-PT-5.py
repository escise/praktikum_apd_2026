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
            os.system("cls")
            print("𝚃𝚎𝚛𝚒𝚖𝚊 𝚔𝚊𝚜𝚒𝚑 𝚝𝚎𝚕𝚊𝚑 𝚖𝚎𝚗𝚐𝚐𝚞𝚗𝚊𝚔𝚊𝚗 𝚂𝚒𝚜𝚝𝚎𝚖 𝙿𝚎𝚗𝚍𝚊𝚝𝚊𝚊𝚗 𝚂𝚝𝚘𝚔 𝙱𝚊𝚛𝚊𝚗𝚐 𝙴𝚕𝚎𝚔𝚝𝚛𝚘𝚗𝚒𝚔!")
            exit()
        else:
            os.system("cls")
            print("angka invalid")
    else:
        os.system("cls")
        print("Input harus berupa angka")

while reg:
    rgs_user = input("masukkan user registrasi baru anda: ").strip().lower()
    rgs_pass = input("masukkan password registrasi baru anda: ")

    if rgs_pass.isdigit():
        user_ada = False
        if rgs_user == user_pw_admin[0]:
            user_ada = True
        else:
            for i in user_pw:
                if i[0] == rgs_user:
                    user_ada = True
                    break
        
        if user_ada:
            print("Username sudah terdaftar!")
        else:
            user_pw = user_pw + ([rgs_user, rgs_pass],)
            os.system("cls")

            rgs_cb = input("Apakah anda ingin login atau registrasi akun baru lagi? (ya/tidak): ").strip().lower()

            if rgs_cb in ["y", "ya", "iya", "yes", "1"]:
                print("silahkan isi akun baru lagi.")
            elif rgs_cb in ["n", "tidak", "tak", "no", "t", "0"]:
                print("silahkan login.")
                log = True
                break
    else:
        os.system("cls")
        print("password yang akan digunakan harus berupa angka.")

while percobaan < 3 and log:
    log_user = input("Masukkan username anda: ").strip().lower()
    log_pw = input("Masukkan password anda: ")
    
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
    
    opsi_in_menu = input("Masukkan Opsi Anda (1-5): ")

    if not opsi_in_menu.isdigit() or not opsi_in_menu:
        print("Input Harus berupa angka atau tidak boleh kosong.")
    else:
        opsi_in_menu = int(opsi_in_menu)
        
        # read
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
            back = input("Back? (tekan enter): ").strip().lower()
            os.system("cls")
            
        # create
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

                        if not (st_br_baru.isdigit() and nm_br_baru and mrk_br_baru and hrg_br_baru.isdigit()):
                            os.system("cls")
                            print("Salah satu atau lebih masukkan tidak valid")
                        else:
                            list_br_elektronik.append([nm_br_baru, mrk_br_baru, f"Rp.{hrg_br_baru}", int(st_br_baru)])
                            dua_lagi = input("Apakah Anda ingin menambahkan Barang Elektronik Baru lagi? (y/n): ").strip().lower()
                            
                            if dua_lagi == "y":
                                os.system("cls")
                            else:
                                os.system("cls")
                                print("masukkan di terima.")
                                break
                else:       
                    os.system("cls")
            else:
                os.system("cls")
                print("Anda bukan seorang admin")
                
        # Update
        elif opsi_in_menu == 3:
            if admin_privilege:
                os.system("cls")
                konfirmasi = input("Apakah Anda ingin mengupdate Stok Barang Elektronik? (y/n): ").lower().strip()
                
                if konfirmasi == "y":
                    while True:
                        os.system("cls")
                        print("=== List Barang Elektronik untuk Diupdate ===")
                        if not list_br_elektronik:
                            print("List barang elektronik kosong.")
                            input("Tekan Enter untuk kembali...")
                            break
                            
                        for i, (a, b, c, d) in enumerate(list_br_elektronik, start=1):
                            print(f"{i}. Nama: {a} | Brand: {b} | Harga: {c} | Stok: {d}")
                        
                        pilih_idx = input("\nPilih nomor barang yang ingin diupdate (ketik 'x' untuk kembali): ").strip()
                        
                        if pilih_idx.lower() == 'x':
                            os.system("cls")
                            break
                            
                        if pilih_idx.isdigit():
                            pilih_idx = int(pilih_idx)
                            if 1 <= pilih_idx <= len(list_br_elektronik):
                                idx = pilih_idx - 1
                                print(f"\n[Mengupdate: {list_br_elektronik[idx][0]}]")
                                print("Tekan Enter jika tidak ingin mengubah suatu kolom.")
                                
                                nm_br_upd = input(f"Nama Barang Baru [{list_br_elektronik[idx][0]}]: ").strip()
                                mrk_br_upd = input(f"Nama Merek Baru [{list_br_elektronik[idx][1]}]: ").strip()
                                hrg_br_upd = input(f"Harga Barang Baru [{list_br_elektronik[idx][2]}]: ").strip()
                                st_br_upd = input(f"Sisa Stok Baru [{list_br_elektronik[idx][3]}]: ").strip()
                                
                                nm_br_upd = nm_br_upd if nm_br_upd else list_br_elektronik[idx][0]
                                mrk_br_upd = mrk_br_upd if mrk_br_upd else list_br_elektronik[idx][1]
                                
                                if not hrg_br_upd:
                                    hrg_br_upd = list_br_elektronik[idx][2]
                                else:
                                    hrg_br_upd = f"Rp.{hrg_br_upd}" if not hrg_br_upd.startswith("Rp.") else hrg_br_upd
                                        
                                if not st_br_upd:
                                    st_br_upd = list_br_elektronik[idx][3]
                                else:
                                    st_br_upd = int(st_br_upd) if st_br_upd.isdigit() else list_br_elektronik[idx][3]
                                        
                                list_br_elektronik[idx] = [nm_br_upd, mrk_br_upd, hrg_br_upd, st_br_upd]
                                os.system("cls")
                                print("Data barang berhasil diupdate!\n")
                                
                                lagi = input("Apakah ingin mengupdate barang lain? (y/n): ").strip().lower()
                                if lagi != "y":
                                    os.system("cls")
                                    break
                            else:
                                print("Nomor barang tidak ada dalam jangkauan.")
                                input("Tekan Enter untuk lanjut...")
                        else:
                            print("Input harus berupa angka.")
                            input("Tekan Enter untuk lanjut...")
                else:
                    os.system("cls")
            else:
                os.system("cls")
                print("Anda bukan seorang admin")
                
        # delete part
        elif opsi_in_menu == 4:
            if admin_privilege:
                os.system("cls")
                konfirmasi = input("Apakah Anda ingin menghapus Stok Barang Elektronik? (y/n): ").lower().strip()
                
                if konfirmasi == "y":
                    while True:
                        os.system("cls")
                        print("=== List Barang Elektronik untuk Dihapus ===")
                        if not list_br_elektronik:
                            print("List barang elektronik kosong.")
                            input("Tekan Enter untuk kembali...")
                            break
                            
                        for i, (a, b, c, d) in enumerate(list_br_elektronik, start=1):
                            print(f"{i}. Nama: {a} | Brand: {b} | Harga: {c} | Stok: {d}")
                        
                        pilih_idx = input("\nPilih nomor barang yang ingin dihapus (ketik 'x' untuk kembali): ").strip()
                        
                        if pilih_idx.lower() == 'x':
                            os.system("cls")
                            break
                            
                        if pilih_idx.isdigit():
                            pilih_idx = int(pilih_idx)
                            if 1 <= pilih_idx <= len(list_br_elektronik):
                                idx = pilih_idx - 1
                                barang_dihapus = list_br_elektronik.pop(idx)
                                os.system("cls")
                                print(f"Barang '{barang_dihapus[0]}' berhasil dihapus!\n")
                                
                                lagi = input("Apakah ingin menghapus barang lain? (y/n): ").strip().lower()
                                if lagi != "y":
                                    os.system("cls")
                                    break
                            else:
                                print("Nomor barang tidak ada dalam jangkauan.")
                        else:
                            print("Input harus berupa angka.")
                else:
                    os.system("cls")
            else:
                os.system("cls")
                print("Anda bukan seorang admin")
        elif opsi_in_menu == 5:
            os.system("cls")
            print("𝚃𝚎𝚛𝚒𝚖𝚊 𝚔𝚊𝚜𝚒𝚑 𝚝𝚎𝚕𝚊𝚑 𝚖𝚎𝚗𝚐𝚐𝚞𝚗𝚊𝚔𝚊𝚗 𝚂𝚒𝚜𝚝𝚎𝚖 𝙿𝚎𝚗𝚍𝚊𝚝𝚊𝚊𝚗 𝚂𝚝𝚘𝚔 𝙱𝚊𝚛𝚊𝚗𝚐 𝙴𝚕𝚎𝚔𝚝𝚛𝚘𝚗𝚒𝚔!")
            exit()
        else:
            print("angka tidak ada dalam jangkauan")