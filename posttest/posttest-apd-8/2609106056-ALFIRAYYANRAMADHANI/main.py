import os
from tampilan import menu_awal, menu_utama
from data_user import user_pw, admin
from auth import reg, login
from data_barang import list_br_elektronik
from prettytable import PrettyTable, ALL

def create(daftar_br, nama, brand, harga, stok):
    nama_b = nama.strip()
    brand_b = brand.strip()
    stok_a = int(stok)
    item_baru = {                        
        "nama": nama_b,
        "brand": brand_b,
        "harga": harga,
        "stok": stok_a
    }
    daftar_br.append(item_baru)
    return daftar_br

def read():
    tampilan_tabel = PrettyTable()
    tampilan_tabel.field_names = ["No", "Nama Barang", "Merk", "Harga", "Stok"]
    
    tampilan_tabel.hrules = ALL

    curr = []
    for i, item in enumerate(list_br_elektronik, start=1):
        harga_angka = float(item['harga'])
        hrg_curr = f"Rp.{harga_angka:,.2f}"
        
        curr.append([
            i,
            item['nama'],
            item['brand'],
            hrg_curr,
            item['stok']
        ])
    
    tampilan_tabel.add_rows(curr)
    print(tampilan_tabel)

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

os.system("cls")

log = False
admin_privilege = False
percobaan_login = 0

while not log and percobaan_login < 3:
    pilih = menu_awal()
    if pilih == "Register":
        os.system("cls")
        reg(user_pw, admin())
    elif pilih == "Login":
        os.system("cls")
        log, admin_privilege, percobaan_login = login(user_pw, admin(), percobaan_login)
        if not log and percobaan_login == 3:
            print("Anda telah gagal login 3 kali.")
            exit()
    elif pilih == "Keluar dari sistem":
        os.system("cls")
        print("𝚃𝚎𝚛𝚒𝚖𝚊 𝚔𝚊𝚜𝚒𝚑 𝚝𝚎𝚕𝚊𝚑 𝚖𝚎𝚗𝚐𝚐𝚞𝚗𝚊𝚔𝚊𝚗 𝚂𝚒𝚜𝚝𝚎𝚖 𝙿𝚎𝚗𝚍𝚊𝚝𝚊𝚊𝚗 𝚂𝚝𝚘𝚔 𝙱𝚊𝚛𝚊𝚗𝚐 𝙴𝚕𝚎𝚔𝚝𝚛𝚘𝚗𝚒𝚔!")
        exit()

os.system("cls")

while True:
    opsi = menu_utama()

    if opsi == '1. Buka List Stok Barang Elektronik':
        os.system("cls")
        read()
        input("\nTekan Enter untuk kembali: ")
        os.system("cls")
    elif opsi == "2. Tambah Stok Barang Elektronik Baru (Admin)":
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
    elif opsi == '3. Update Stok Barang Elektronik (Admin)':
        os.system("cls")
        if admin_privilege:
            try:
                konfirmasi = input("Apakah Anda ingin mengubah data Barang Elektronik? (y/n): ").lower().strip()
                
                if konfirmasi == "y":
                    while True:
                        print()
                        read()
                        if list_br_elektronik:
                            pilih_idx = input("\nPilih nomor barang yang ingin diupdate/ubah: ").strip()
                            try:
                                if not pilih_idx.isdigit():
                                    raise ValueError("Input harus berupa angka.")
                                pilih_idx = int(pilih_idx)
                                
                                if 1 <= pilih_idx <= len(list_br_elektronik):
                                    idx = pilih_idx - 1
                                    curr = list_br_elektronik[idx]
                                    print(f"\n[Mengubah: {curr['nama']}] Kosongkan jika tidak ingin mengubah.")
                                    
                                    nm = input(f"Nama Baru [{curr['nama']}]: ").strip()
                                    brd = input(f"Brand Baru [{curr['brand']}]: ").strip()
                                    hrg = input(f"Harga Baru [{curr['harga']}]: ").strip()
                                    stk = input(f"Stok Baru [{curr['stok']}]: ").strip()
                                    
                                    list_br_elektronik = update(list_br_elektronik, idx, nm, brd, hrg, stk)
                                    print("Data barang elektronik berhasil di update/ubah!")

                                    lagi = input("Apakah ingin mengubah barang lain? (y/n): ").strip().lower()
                                    if lagi != "y":
                                        os.system("cls")
                                        break
                                    os.system("cls")
                                else:
                                    print("Nomor barang tidak ada atau tidak valid.")
                            except ValueError:
                                print("Input harus berupa angka.")
                else:
                    os.system("cls")
            except ValueError:
                print("Input tidak diketahui.")
                input("\nTekan Enter untuk kembali: ")
        else:
            print("Anda bukan seorang admin")
        input("\nTekan Enter untuk kembali: ")
        os.system("cls")
    elif opsi == '4. Hapus Stok Barang Elektronik (Admin)':
        os.system("cls")
        if admin_privilege:
            try:
                konfirmasi = input("Apakah Anda ingin menghapus data Barang Elektronik? (y/n): ").lower().strip()
                
                if konfirmasi == "y":
                    while True:
                        print()
                        read()
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

                                    lagi = input("Apakah ingin menghapus barang lain? (y/n): ").strip().lower()
                                    if lagi != "y":
                                        os.system("cls")
                                        break 
                                    os.system("cls")
                                else:
                                    print("Nomor barang tidak valid.")
                            except ValueError:
                                print("Input harus berupa angka.")
                else:
                    os.system("cls")
            except ValueError:
                print("Input tidak diketahui.")
                input("\nTekan Enter untuk kembali: ")
        else:
            print("Anda bukan seorang admin.")
        input("\nTekan Enter untuk kembali: ")
        os.system("cls")
    elif opsi == '5. Total Stok Keseluruhan':
        os.system("cls")
        total_stok2 = total_stok(list_br_elektronik)
        print(f"Total seluruh stok barang elektronik di sistem: {total_stok2} unit")
        input("\nTekan Enter untuk kembali: ")
        os.system("cls")
    elif opsi == '6. Keluar dari Program':
        os.system("cls")
        print("𝚃𝚎𝚛𝚒𝚖𝚊 𝚔𝚊𝚜𝚒𝚑 𝚝𝚎𝚕𝚊𝚑 𝚖𝚎𝚗𝚐𝚐𝚞𝚗𝚊𝚔𝚊𝚗 𝚂𝚒𝚜𝚝𝚎𝚖 𝙿𝚎𝚗𝚍𝚊𝚝𝚊𝚊𝚗 𝚂𝚝𝚘𝚔 𝙱𝚊𝚛𝚊𝚗𝚐 𝙴𝚕𝚎𝚔𝚝𝚛𝚘𝚗𝚒𝚔!")
        break