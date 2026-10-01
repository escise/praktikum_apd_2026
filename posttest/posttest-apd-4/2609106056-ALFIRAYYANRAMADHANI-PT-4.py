username = "alfi"
password = 56
percobaan = 0

while percobaan < 3:
    username_login = input("Masukkan username anda: ").strip().lower()
    password_login = int(input("Masukkan password anda: "))

    if username_login == "alfi":
        if password_login == 56:
            print('''
            --Login Berhasil!--

                ==========================================

                Opsi 1 -> Paket Reguler, 1 porsi makanan.
                Opsi 2 -> Paket Anak, 1 porsi makanan.
                Opsi 3 -> Paket Keluarga, 4 porsi makanan.
                Opsi 4 -> Keluar dari program.

                ==========================================
            ''')

            total_porsi = 0
            total_paket = 0

            for i in range(999999):
                masukkan_opsi = int(input("Masukkan angka untuk memilih opsi (1-4): "))

                if masukkan_opsi == 1:
                    print("Paket Reguler telah terpilih dengan satu porsi makanan.")
                    total_porsi += 1
                    total_paket += 1
                elif masukkan_opsi == 2:
                    print("Paket Anak telah terpilih dengan satu porsi makanan.")
                    total_porsi += 1
                    total_paket += 1
                elif masukkan_opsi == 3:
                    print("Paket Keluarga telah terpilih dengan empat porsi makanan.")
                    total_porsi += 4
                    total_paket += 1
                elif masukkan_opsi == 4:
                    if total_porsi >= 20:
                        print(f'''
                        ''')
                    elif total_porsi >= 10 and total_porsi < 20:
                        print(f'''
                        ''')
                    elif total_porsi >= 5 and total_porsi <10:
                        print(f'''
                        ''')
                    else:
                        print(f'''
                        ''')
                    break
                else:
                    print("Opsi tidak valid")
            break
        else:
            percobaan += 1
            print("password salah")
    else:
        percobaan += 1
        print("Username salah.")
if percobaan == 3:
    print("anda gagal login tiga kali")