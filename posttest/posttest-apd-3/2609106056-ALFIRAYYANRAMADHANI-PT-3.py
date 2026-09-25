nama = "alfi"
nim = 56

login_user = input("masukkan username: ").lower().strip()
login_password = int(input("masukkan password: "))

if login_user == nama:
    if login_password == nim:
        print("login berhasil!")
        total_point = int(input("masukkan poin rank: "))
        if total_point < 100:
            if total_point >= 0:
                selisih = 100 - total_point
                print(f'''
                User              : {nama}
                Rank              : Rookie
                poin untuk rank up: {selisih}
                ''')
            else:
                print("Error: Poin tidak boleh dibawah 0")
        elif total_point >= 100 and total_point <= 299:
            selisih = 300 - total_point
            print(f'''
            User              : {nama}
            Rank              : Warrior
            poin untuk rank up: {selisih}
            ''')
        elif total_point >= 300 and total_point <= 999:
            selisih = 1000 - total_point
            print(f'''
            User              : {nama}
            Rank              : Master
            poin untuk rank up: {selisih}
            ''')
        elif total_point >= 1000 and total_point <= 4999:
            selisih = 5000 - total_point
            print(f'''
            User              : {nama}
            Rank              : Grand Master
            poin untuk rank up: {selisih}
            ''')
        elif total_point >= 5000:
            print(f'''
            User              : {nama}
            Rank              : Legend
            Selamat! Anda mencapai rank tertinggi saat ini!
            ''')
    else:
        print("Error: user atau password salah")
else:
    # disamain ajah biar gak mudah di tebak loginnya
    print("Error: user atau password salah")
