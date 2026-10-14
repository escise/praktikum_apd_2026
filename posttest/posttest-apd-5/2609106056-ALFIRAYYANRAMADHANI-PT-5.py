import os

user_admin = "alfi"
pw_admin = 2008
user_pw = ()
reg = False
log = False

percobaan = 0

list_br_elektronik = []

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
            break
        elif rgs == 3:
            exit()
        else:
            os.system("cls")
            print('''
            angka invalid
            ''')
    else:
        os.system("cls")
        print("Input harus berupa angka")

while reg:
    rgs_user = input("masukkan user registrasi baru anda: ")
    rgs_pass = input("masukkan password registrasi baru anda: ")

    if rgs_pass.isdigit():
        user_pw = user_pw + ([rgs_user, rgs_pass],)
        os.system("cls")

        rgs_cb = input("Apakah anda ingin login atau registrasi akun baru lagi? (ya/tidak): ").strip().lower()

        if rgs_cb in ["y", "ya", "iya", "yes", 1]:
            print("silahkan isi akun baru lagi.")
        elif rgs_cb in ["n", "tidak", "tak", "no", "t", 0]:
            print("silahkan login.")
            break
    else:
        os.system("cls")
        print("password yang akan digunakan harus berupa angka.")

while percobaan < 3 and log:
    log_user = input("Masukkan username anda: ").strip().lower()
    log_pw = input("Masukkan password anda: ")