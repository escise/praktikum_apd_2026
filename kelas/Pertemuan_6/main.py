# bentuk set
kartu = {"merah", "merah", "biru", "hijau"}
print(kartu)

# set menggunakan list
matkul = ["apd", "orsikom", "apd", "kalkulus"]
sks = set(matkul)
print(sks)

# set menggunakan tuple
buah = set(("apel", "jeruk", "mangga", "apel"))
print(buah)

# mengakses elemen pada set
angka_ganjil = {1, 3, 5, 7, 9}
for angka in angka_ganjil:
    print (angka)

# menambahkan elemen pada set
kelas = {"a", "b", "c"}
kelas.add("d")
print(kelas)

# menghapus elemen pada set
buah = {"apel", "mangga", "jeruk"}
buah.discard("mangga")
print(buah)

# Himpunan pada set, menggunakan union()
aslab1 = {"fina", "shasha", "risma"}
aslab2 = {"larry", "attar", "haekal"}
gabung = aslab1.union(aslab2)
print(gabung)

# menggunakan update()
aslab1 = {"fina", "shasha", "risma"}
aslab2 = {"larry", "attar", "haekal"}
aslab1.update(aslab2)
print(aslab1)

# menggunakan difference()
aslab1 = {"fina", "shasha", "risma"}
aslab2 = {"larry", "attar", "haekal"}
perbedaan = aslab1.difference(aslab2)
print(perbedaan)

# menggunakan intersection()
aslab1 = {"fina", "shasha", "risma", "attar"}
aslab2 = {"larry", "attar", "haekal"}
irisan = aslab1.intersection(aslab2)
print(irisan)


# Dictionary
Matkul = {
    "Matkul_ganjil" : "kalkulus",
    "Matkul_genap" : "statistik"
}
print(Matkul["Matkul_ganjil"])
print(Matkul)

Biodata = {
"Nama" : "Siti Julpa",
"NIM" : 25091060,
"KRS" : ["Struktur Data", "Basis Data"],
"Mahasiswa_Aktif" : True,
"Instagram" : "julpatarr"
}

print(f"Nama saya adalah {Biodata['Nama']}")
print(f"Saya mengambil mata kuliah {Biodata['KRS'][0]} dan {Biodata['KRS'][1]}")

# menggunakan parameter dict
List_game = dict(Genshin_Impact="Open World", Mole="Moba",
Stardew_Valley="Farming Simulation")

# perulangan dictionary
game = {
"pou" : "chill",
"genshin impact" : "action",
"valorant" : "fps",
"minecraft" : "sandbox",
"mobile legend" : "moba"
}

# for i in game.values():
#     print(i)

# for key, value in game.items():
#     print(key, value)

game["resident evil"] = "Horror"
print(game)

game.update({"Roblox" : "Sandbox"})
print(game)

item = game.setdefault("PUBG", "fps")
print(game)


aset = {
"jenis" : "rumah",
"harga" : 120000000,
"alamat" : "Jl. Raya No. 1",
"berpenghuni" : True,
"luas" : "120m x 80m"
}

print(aset)
del aset["luas"]
print(aset)
print(aset.get("luas"))

print(aset)
cache = aset.pop("berpenghuni")
print(aset)
print(aset.get("berpenghuni"))
print(cache)

print(aset)
aset.clear()
print(aset)

print("Panjang dictionary :", len(aset))
print(len(aset))


menu = {
"ayam geprek" : 15000,
"ayam goreng" : 13000,
"ayam bakar" : 17000,
"nasi goreng" : 12000,
"mie goreng" : 10000
}

menu_baru = menu.copy()
menu_baru["nasi goreng"] = 15000
print(menu)
print(menu_baru)

key = "ayam geprek", "ayam goreng", "ayam bakar",
value = 12000

menu = dict.fromkeys(key, value)
print(menu)

menu = {
"ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
"nasi" : ["nasi goreng", "nasi uduk"],
"mie" : ["mie goreng rendang", "mie goreng aceh"],
"kuah" : ["soto", "rawon", "sop iga"]
}
for i, j in menu.items():
    print(f"Kategori {i} memiliki menu :")
    for kategori in j:
        print(kategori)
    print("")
