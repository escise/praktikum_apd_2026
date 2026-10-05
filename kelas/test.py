username = "alfi"
password = 56
percobaan = 0
login_benar = False

while percobaan < 3:
    login_username = input("masukkan username anda: ").strip().lower()
    login_password = input("masukkan password anda: ").strip()

    if not login_username or not login_password:
        print("Input tidak boleh kosong.")
        continue
    
    if not login_password.isdigit():
        print("Password harus berupa angka.")
        continue

    login_password = int(login_password)

    if login_username == username:
        if login_password == password:
            login_benar = True
            print("Login berhasil!")
            break
        else:
            percobaan += 1
            print("password salah.")
    else:
        percobaan += 1
        print("username salah.")

    if percobaan == 3:
        print("Telah gagal login sebanyak tiga kali")
        exit()

total_porsi = 0
total_paket = 0
nama_paket_terakhir = "-"

while login_benar:
    print('''
    ============= MENU ==============

    1. PAKET REGULAR     (1 Porsi/paket)
    2. PAKET ANAK        (1 Porsi/paket)
    3. PAKET KELUARGA    (4 Porsi/paket)
    4. KONFIRMASI PESANAN

    =================================
    ''')
    opsi_input = input("Pilih salah satu opsi (1-4): ")
                
    if not opsi_input:
        print("Input tidak boleh kosong.")
        continue
    elif not opsi_input.isdigit():
        print("Input harus berbentuk angka")
        continue

    opsi_inte = int(opsi_input)

    if opsi_inte < 1 or opsi_inte > 4:
        print("Opsi tidak valid")
        continue

    if opsi_inte == 4:
        print("terima kasih telah menggunakan pelayanan kami")
        break

    if opsi_inte == 1:
        nama_paket = "Paket Reguler"
        porsi = 1
    elif opsi_inte == 2:
        nama_paket = "Paket Anak"
        porsi = 1
    else:
        nama_paket = "Paket Keluarga"
        porsi = 4

    nama_paket_terakhir = nama_paket

    while True:
        jumlah_paket = input(f"masukkan jumlah {nama_paket} yang telah anda pilih: ").strip()

        if not jumlah_paket:
            print("Input tidak boleh kosong")
            continue
        elif not jumlah_paket.isdigit():
            print("Input harus berbentuk angka")
            continue

        jumlah_paket_inte = int(jumlah_paket)
        if jumlah_paket_inte <= 0:
            print("Jumlah Paket harus lebih dari 0")
            continue
        break

    total_paket += jumlah_paket_inte
    for i in range(jumlah_paket_inte):
        total_porsi += porsi

if login_benar and total_porsi > 0:
    if total_porsi >= 20:
        bonus = "5 paket buah"
    elif total_porsi >= 10:
        bonus = "3 botol susu"
    elif total_porsi >= 5:
        bonus = "1 paket vitamin"
    else:
        bonus = "gak ada bonus"

    # asumsi jumlah penerima itu sama dengan total porsi, adalah pokoknya
    print(f'''
        ============= KUITANSI ==============
    
            Jenis Paket     :   {nama_paket_terakhir}
            Jumlah Paket    :   {total_paket}
            Total Porsi     :   {total_porsi} porsi
            Jumlah Penerima :   {total_porsi} orang
            Bonus           :   {bonus}

        =====================================
    ''')