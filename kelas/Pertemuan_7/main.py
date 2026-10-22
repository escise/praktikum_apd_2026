# def nama_fungsi():
#     pernyataan
#     return hasil yang diinginkan

# def luas_persegi_panjang():
#     luas = 3 * 5
#     return luas
# # Kita panggil fungsinya
# print("Luas persegi panjang:", luas_persegi_panjang())

# def sapa():
#     print("Haloooo alfi")
# sapa()

# # def sapa():
# #     return "Haloooo alfi"

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# # Kita panggil fungsinya lalu argumen kita adalah angka 7
# print("Luas persegi:", luas_persegi(7))

# def persegi(sisi):
#     hasil = sisi*sisi
#     return hasil

# print(persegi(5))

# def menu():
#     print("1. Create")
#     print("2. Read")
#     print("3. Update")
#     print("4. Delete")

#     pilihan = input("pilih menu: ")

# nama = "Larry"
# prodi = "Informatika"
# #Membuat variabel lokal
# def data():
#     nama = "anu"
#     prodi = "Kedokteran Lanjut"
#     print("Nama:", nama)
#     print("Prodi:", prodi)

def faktorial(n):
#Base Case: Kondisi fungsi berhenti
    if n == 0 or n == 1:
        return 1
    #Rekursive Case: Fungsi memanggil dirinya sendiri
    else:
        return n * faktorial(n - 1)
#Memanggil fungsi
hasil_faktorial = faktorial(4)
print(f"Hasil dari 4! {hasil_faktorial}")


try:
    umur = int(input("umur anda: "))
except ValueError:
    print("input tidak di ketahui.")
else:
    print(umur)
finally:
    print("selesai")

try:
    usn = input('Username yang diinginkan : ')
    if len(usn) < 5:
        raise ValueError('Nama Minimal Memiliki 5 karakter')
except ValueError as e:
    print(e)

