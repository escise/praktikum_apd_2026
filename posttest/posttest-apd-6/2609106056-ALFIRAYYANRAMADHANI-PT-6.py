import os

user_pw_admin = ("alfi", "2008")
user_pw = {}

reg = False
log = False
admin_privilege = False

percobaan = 0

list_br_elektronik = [
    {"nama": "Laptop Ideapad", "brand": "Legowo", "harga": "Rp.10000000", "stok": 5},
    {"nama": "Iphonk 67", "brand": "Apel", "harga": "Rp.99000000", "stok": 2},
    {"nama": "Tab Samsul", "brand": "Samsul", "harga": "Rp.10000000", "stok": 1},
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
        if rgs_user in user_pw or rgs_user == user_pw_admin[0]:
            print("Username tidak boleh sama atau sudah terdaftar!")
        else:
            user_pw[rgs_user] = rgs_pass
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
    elif log_user in user_pw and user_pw[log_user] == log_pw:
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
        
        #Read
        if opsi_in_menu == 1:
            os.system("cls")
            print("list barang elektronik")
            for i in list_br_elektronik:
                print(f'''
                Nama Barang : {i["nama"]}
                Nama Brand  : {i["brand"]}
                Harga Barang: {i["harga"]}
                 Stok       : {i["stok"]}
                ''')
            back = input("Back? ").strip().lower()
            os.system("cls")
            
        #Create
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
                            barang_baru = {
                                "nama": nm_br_baru,
                                "brand": mrk_br_baru,
                                "harga": f"Rp.{hrg_br_baru}",
                                "stok": int(st_br_baru)
                            }
                            list_br_elektronik.append(barang_baru)
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
                
        #Update
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
                            
                        for i, item in enumerate(list_br_elektronik, start=1):
                            print(f"{i}. Nama: {item['nama']} | Brand: {item['brand']} | Harga: {item['harga']} | Stok: {item['stok']}")
                        
                        pilih_idx = input("\nPilih nomor barang yang ingin diupdate (ketik 'b' untuk kembali): ").strip()
                        
                        if pilih_idx.lower() == 'b':
                            os.system("cls")
                            break
                            
                        if pilih_idx.isdigit():
                            pilih_idx = int(pilih_idx)
                            if 1 <= pilih_idx <= len(list_br_elektronik):
                                idx = pilih_idx - 1
                                current_item = list_br_elektronik[idx]
                                print(f"\n[Mengupdate: {current_item['nama']}]")
                                print("Tekan Enter langsung jika tidak ingin mengubah suatu kolom.")
                                
                                nm_br_upd = input(f"Nama Barang Baru [{current_item['nama']}]: ").strip()
                                mrk_br_upd = input(f"Nama Merek Baru [{current_item['brand']}]: ").strip()
                                hrg_br_upd = input(f"Harga Barang Baru [{current_item['harga']}]: ").strip()
                                st_br_upd = input(f"Sisa Stok Baru [{current_item['stok']}]: ").strip()
                                
                                nm_br_upd = nm_br_upd if nm_br_upd else current_item['nama']
                                mrk_br_upd = mrk_br_upd if mrk_br_upd else current_item['brand']
                                
                                if not hrg_br_upd:
                                    hrg_br_upd = current_item['harga']
                                else:
                                    hrg_br_upd = f"Rp.{hrg_br_upd}" if not hrg_br_upd.startswith("Rp.") else hrg_br_upd
                                        
                                if not st_br_upd:
                                    st_br_upd = current_item['stok']
                                else:
                                    st_br_upd = int(st_br_upd) if st_br_upd.isdigit() else current_item['stok']
                                        
                                list_br_elektronik[idx] = {
                                    "nama": nm_br_upd,
                                    "brand": mrk_br_upd,
                                    "harga": hrg_br_upd,
                                    "stok": st_br_upd
                                }
                                os.system("cls")
                                print("Data barang berhasil diupdate!\n")
                                
                                lagi = input("Apakah ingin mengupdate barang lain? (y/n): ").strip().lower()
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
                print("Anda bukan seorang admin")
                
        #deletee
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
                            
                        for i, item in enumerate(list_br_elektronik, start=1):
                            print(f"{i}. Nama: {item['nama']} | Brand: {item['brand']} | Harga: {item['harga']} | Stok: {item['stok']}")
                        
                        pilih_idx = input("\nPilih nomor barang yang ingin dihapus (ketik 'b' untuk kembali): ").strip()
                        
                        if pilih_idx.lower() == 'b':
                            os.system("cls")
                            break
                            
                        if pilih_idx.isdigit():
                            pilih_idx = int(pilih_idx)
                            if 1 <= pilih_idx <= len(list_br_elektronik):
                                idx = pilih_idx - 1
                                barang_dihapus = list_br_elektronik.pop(idx)
                                os.system("cls")
                                print(f"Barang '{barang_dihapus['nama']}' berhasil dihapus!\n")
                                
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
                
        #Exit
        elif opsi_in_menu == 5:
            os.system("cls")
            print("𝚃𝚎𝚛𝚒𝚖𝚊 𝚔𝚊𝚜𝚒𝚑 𝚝𝚎𝚕𝚊𝚑 𝚖𝚎𝚗𝚐𝚐𝚞𝚗𝚊𝚔𝚊𝚗 𝚂𝚒𝚜𝚝𝚎𝚖 𝙿𝚎𝚗𝚍𝚊𝚝𝚊𝚊𝚗 𝚂𝚝𝚘𝚔 𝙱𝚊𝚛𝚊𝚗𝚐 𝙴𝚕𝚎𝚔𝚝𝚛𝚘𝚗𝚒𝚔!")
            exit()
        else:
            print("angka tidak ada dalam jangkauan")