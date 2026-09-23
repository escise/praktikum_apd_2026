cuaca = "hujan"

if cuaca == "hujan":
    print("bawa payung/jas hujan")
    print("telat dikittt")

print("otw ke kampus")


budget = 20000
cuaca = "hujan"

if budget > 30000 and cuaca == "cerah":
    print("beli Yoshinoya")
else:
    print("masak indomie aja")


kendaraan = input("masukkan jenis kendaraan anda: ").lower().strip()

if kendaraan == "mobil":
    tarif_parkir = 10000
elif kendaraan == "motor":
    tarif_parkir = 5000
else:
    tarif_parkir = 15000

print("tarif parkir yang harus dibayar adalah: ", tarif_parkir)


bilangan = -5
status = "bilangan negatif" if bilangan < 0 else "bilangan positif"
print(status)


username = input("masukkan username: ").lower().strip()
password = input("masukkan password: ").lower().strip()

if username == "alfi":
    if password == "056":
        print("login berhasil")
    else:
        print("password salah")
else:
    print("username salah")


angka = 10 / 6
print(f"angka {angka:.02f}")