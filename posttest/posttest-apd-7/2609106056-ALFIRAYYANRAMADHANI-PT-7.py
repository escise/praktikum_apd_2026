import os

user_pw_admin = ("alfi", "2008")
user_pw = {}
list_br_elektronik = [
    {"nama": "Laptop Ideapad", "brand": "Legowo", "harga": "Rp.10000000", "stok": 5},
    {"nama": "Iphonk 67", "brand": "Apel", "harga": "Rp.99000000", "stok": 2},
    {"nama": "Tab Samsul", "brand": "Samsul", "harga": "Rp.10000000", "stok": 1},
]

os.system("cls")

def menu_awal():
    print("Pilih Metode Login anda")
    print("1. Register")
    print("2. Login")
    print("3. Keluar dari sistem")

def menu_utama():
    print('''
        =============== Selamat Datang ================
        
        1. Buka List Stok Barang Elektronik
        2. Tambah Stok Barang Elektronik Baru (Admin)
        3. Update Stok Barang Elektronik (Admin)
        4. Hapus Stok Barang Elektronik (Admin)
        5. Total stok keseluruhan
        6. Keluar dari Program
        
        ===============================================
    ''')
    opsi = input("Masukkan pilihan menu (1-6): ")
    return opsi

def admin():
    return user_pw_admin

def login(username, password, database):
    if username in database and database[username] == password:
        return True
    return False

def create(daftar_br, nama, brand, harga, stok):
    nama_b = nama.strip()
    brand_b = brand.strip()
    harga_f = f"Rp.{harga.strip()}"
    stok_a = int(stok)
    item_baru = {                        
        "nama": nama_b,
        "brand": brand_b,
        "harga": harga_f,
        "stok": stok_a
    }
    daftar_br.append(item_baru)
    return daftar_br

def read(daftar_barang):
    print('''\n=== DAFTAR STOK BARANG ELEKTRONIK ===''')
    if not daftar_barang:
        print("Stok barang elektronik tidak ada")
        return
    for i, item in enumerate(daftar_barang, start=1):
        print(f"{i}. Nama: {item['nama']} | Brand: {item['brand']} | Harga: {item['harga']} | Stok: {item['stok']}")
    print()

def update(daftar_br, i, nama_b, brand_b, harga_b, stok_b):
    item_l = daftar_br[i]
    
    nm = nama_b if nama_b else item_l['nama']
    brd = brand_b if brand_b else item_l['brand']
    
    if not harga_b:
        hrg = item_l['harga']
    else:
        hrg = f"Rp.{harga_b}" if not harga_b.startswith("Rp.") else harga_b
        
    stk = int(stok_b) if stok_b.isdigit() else item_l['stok']
    
    daftar_br[i] = {
        "nama": nm,
        "brand": brd,
        "harga": hrg,
        "stok": stk
    }
    return daftar_br

def deletes(daftar_br, i):
    barang_delete = daftar_br.pop(i)
    return barang_delete

def total_stok(daftar_br, i=0):
    if i >= len(daftar_br):
        return 0
    return daftar_br[i]["stok"] + total_stok(daftar_br, i + 1)

menu_awal()

log = False
admin_privilege = False
percobaan_login = 0

while not log and percobaan_login < 3:
    try:
        pilih = int(input("Pilih opsi (1-3): "))
    except ValueError:
        print("Input hanya diperbolehkan untuk memasukkan angka.")
        continue

    if pilih == 1:
        reg_user = input("Masukkan username baru: ").strip().lower()
        reg_pw = input("Masukkan password baru (harus angka): ")
        try:
            if not reg_pw.isdigit():
                raise ValueError("Password wajib berupa angka.")
            
            admin_data = admin()
            if reg_user in user_pw or reg_user == admin_data[0]:
                print("Username sudah terdaftar.")
            else:
                user_pw[reg_user] = reg_pw
                print("Registrasi berhasil! Silahkan  login.")
                os.system("cls")
                print(menu_awal())
        except ValueError:
            print("Input tidak valid.")

    elif pilih == 2:
        log_user = input("Username: ").strip().lower()
        log_pw = input("Password: ")
        
        admin_data = admin()
        if log_user == admin_data[0] and log_pw == admin_data[1]:
            print("Login berhasil sebagai admin.")
            admin_privilege = True
            log = True
        else:
            if login(log_user, log_pw, user_pw):
                print("Login berhasil sebagai Pengguna.")
                admin_privilege = True
                log = True
            else:
                print("Username atau password salah!")
                percobaan_login += 1
                if percobaan_login == 3:
                    print("Anda telah gagal login 3 kali.")
                    exit()
    elif pilih == 3:
        os.system("cls")
        print("𝚃𝚎𝚛𝚒𝚖𝚊 𝚔𝚊𝚜𝚒𝚑 𝚝𝚎𝚕𝚊𝚑 𝚖𝚎𝚗𝚐𝚐𝚞𝚗𝚊𝚔𝚊𝚗 𝚂𝚒𝚜𝚝𝚎𝚖 𝙿𝚎𝚗𝚍𝚊𝚝𝚊𝚊𝚗 𝚂𝚝𝚘𝚔 𝙱𝚊𝚛𝚊𝚗𝚐 𝙴𝚕𝚎𝚔𝚝𝚛𝚘𝚗𝚒𝚔!")
        exit()

os.system("cls")

while True:
    opsi = menu_utama()

    try:
        if not opsi.isdigit():
            raise ValueError("Input harus berupa angka.")
        opsi = int(opsi)
    except ValueError:
        print("Input tidak valid.")
        continue

    if opsi == 1:
        os.system("cls")
        read(list_br_elektronik)
        input("\nTekan Enter untuk kembali: ")
        os.system("cls")
    elif opsi == 2:
        os.system("cls")
        if admin_privilege:
            konfirmasi = input("Apakah Anda ingin menambahkan Barang Elektronik Baru? (y/n): ").lower().strip()
            
            if konfirmasi == "y":
                nm = input("Nama barang: ")
                brd = input("Brand barang: ")
                hrg = input("Harga (angka): ")
                stk = input("Stok (angka): ")
                
                try:
                    if not (stk.isdigit() and hrg.isdigit()):
                        raise ValueError("Harga dan Stok wajib berupa angka!")
                    
                    list_br_elektronik = create(list_br_elektronik, nm, brd, hrg, stk)
                    print("Barang baru berhasil ditambahkan")
                except ValueError as r:
                    print(f"Gagal menambahkan barang: {r}")
            else:       
                    os.system("cls")
        else:
            print("Anda bukan seorang admin")
        input("\nTekan Enter untuk kembali: ")
        os.system("cls")

    elif opsi == 3:
        os.system("cls")
        if admin_privilege:
            print()
            read(list_br_elektronik)
            if list_br_elektronik:
                pilih_idx = input("\nPilih nomor barang yang ingin diupdate/ubah: ").strip()
                try:
                    if not pilih_idx.isdigit():
                        raise ValueError("Input harus berupa angka.")
                    pilih_idx = int(pilih_idx)
                    
                    if 1 <= pilih_idx <= len(list_br_elektronik):
                        idx = pilih_idx - 1
                        curr = list_br_elektronik[idx]
                        print(f"\n[Mengupdate: {curr['nama']}] Kosongkan jika tidak ingin mengubah.")
                        
                        nm = input(f"Nama Baru [{curr['nama']}]: ").strip()
                        brd = input(f"Brand Baru [{curr['brand']}]: ").strip()
                        hrg = input(f"Harga Baru [{curr['harga']}]: ").strip()
                        stk = input(f"Stok Baru [{curr['stok']}]: ").strip()
                        
                        list_br_elektronik = update(list_br_elektronik, idx, nm, brd, hrg, stk)
                        print("Data barang elektronik berhasil di update/ubah!")
                    else:
                        print("Nomor barang tidak ada atau tidak valid.")
                except ValueError:
                    print("Input harus berupa angka.")
        else:
            print("Anda bukan seorang admin")
        input("\nTekan Enter untuk kembali: ")
        os.system("cls")

    elif opsi == 4:
        os.system("cls")
        if admin_privilege:
            print("")
            read(list_br_elektronik)
            if list_br_elektronik:
                pilih_idx = input("\nPilih nomor barang yang ingin dihapus: ").strip()
                try:
                    if not pilih_idx.isdigit():
                        raise ValueError("Nomor pilihan harus berupa angka.")
                    pilih_idx = int(pilih_idx)
                    
                    if 1 <= pilih_idx <= len(list_br_elektronik):
                        idx = pilih_idx - 1
                        dihapus = deletes(list_br_elektronik, idx)
                        print(f"Barang '{dihapus['nama']}' berhasil dihapus dari sistem!")
                    else:
                        print("Nomor barang tidak valid.")
                except ValueError:
                    print("Input harus berupa angka.")
        else:
            print("Anda bukan seorang admin.")
        input("\nTekan Enter untuk kembali: ")
        os.system("cls")

    elif opsi == 5:
        os.system("cls")
        total_stok2 = total_stok(list_br_elektronik)
        print(f"Total seluruh stok barang elektronik di sistem: {total_stok2} unit")
        input("\nTekan Enter untuk kembali: ")
        os.system("cls")

    elif opsi == 6:
        os.system("cls")
        print("𝚃𝚎𝚛𝚒𝚖𝚊 𝚔𝚊𝚜𝚒𝚑 𝚝𝚎𝚕𝚊𝚑 𝚖𝚎𝚗𝚐𝚐𝚞𝚗𝚊𝚔𝚊𝚗 𝚂𝚒𝚜𝚝𝚎𝚖 𝙿𝚎𝚗𝚍𝚊𝚝𝚊𝚊𝚗 𝚂𝚝𝚘𝚔 𝙱𝚊𝚛𝚊𝚗𝚐 𝙴𝚕𝚎𝚔𝚝𝚛𝚘𝚗𝚒𝚔!")
        break
    else:
        print("Pilihan menu tidak valid, silakan masukkan angka 1-6.")