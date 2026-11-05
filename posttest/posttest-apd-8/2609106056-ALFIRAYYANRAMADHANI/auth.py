import pwinput as pw
import os
from data_user import admin

def reg(database, admin_data):
    reg_user = input("Masukkan username baru: ").strip().lower()
    reg_pw = pw.pwinput("Masukkan password baru (minimal 8 karakter): ", mask="*")

    try:
        admin_data = admin()

        if reg_user in database or reg_user == admin_data[0]:
            print("Username sudah terdaftar.")

        if not reg_pw or len(reg_pw) < 8:
            raise ValueError("Password tidak boleh kosong atau harus lebih dari 8 karakter.")

        while True:
            c = 0
            konfirmasi = pw.pwinput("konfirmasi password: ", mask="*")
            if konfirmasi == reg_pw:
                break
            print("Password tidak cocok. Silakan coba lagi.")
            c += 1
            if c == 3:
                inp = input("apakah anda ingin mengganti password baru? (y/n): ").strip().lower()
                if inp == 'n':
                    break
                c = 0

        database[reg_user] = reg_pw
        print("Registrasi berhasil! Silahkan login.")
        lanjut = input("tekan enter untuk lanjut: ")
        os.system("cls")
    except ValueError:
        print("Input tidak valid.")
    
def login(database, admin_data, percobaan):
    log_user = input("Username: ").strip().lower()
    log_pw = pw.pwinput("Password: ", mask="*")
    
    if log_user == admin_data[0] and log_pw == admin_data[1]:
        print("Login berhasil sebagai admin!")
        return True, True, percobaan
    else:
        if validasi_login(log_user, log_pw, database):
            print("Login berhasil sebagai Pengguna!")
            return True, False, percobaan
        else:
            os.system("cls")
            print("Username atau password salah!")
            percobaan += 1
            return False, False, percobaan

def validasi_login(username, password, database):
    if username in database and database[username] == password:
        return True
    return False