nama = "alfi"
nim = 56

login_user = input("masukkan username: ").lower().strip()
login_password = input("masukkan username: ")

if login_user == nama:
    if login_password == nim:
        print("login berhasil!")
        total_point = int(input("masukkan poin rank: "))
        if total_point < 100:
            if total_point >= 0:
                selisih = total_point - 100
                print(f'''
                User              : {nama}
                Rank              : Rookie
                poin untuk rank up: {selisih}
                ''')
            else:
                print("Error: Poin tidak boleh dibawah 0")
        elif total_point >= 100 and total_point <= 299:
            selisih = total_point - 300
            print(f'''
            User              : {nama}
            Rank              : Warrior
            poin untuk rank up: {selisih}
            ''')
        elif total_point >= 300 and total_point <= 999:
            selisih = total_point - 1000
            print(f'''
            User              : {nama}
            Rank              : Master
            poin untuk rank up: {selisih}
            ''')
        elif total_point >= 1000 and total_point <= 4999:
            selisih = total_point - 5000
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
            print("sistem error")
    else:
        print("user atau password salah")
else:
    # disamain ajah biar gak mudah di tebak loginnya
    print("user atau password salah")
