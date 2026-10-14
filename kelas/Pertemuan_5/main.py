formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]

print(formula1)

for i, e in enumerate(formula1, start=1):
    print(i, e)

sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
print(sirkuit)

sirkuit.append("Alfi")
print(sirkuit)

sirkuit.append("Kosuzu")
print(sirkuit)

sirkuit.extend(["Leisure", "Ray"])
print(sirkuit)

sirkuit.insert(2, "Rizky")
print(sirkuit)

sirkuit[3] = "Apip"
print(sirkuit)

sirkuit[0:1] = ["Rizky", "Naufal"]
print(sirkuit)

# sirkuit[start:stop:step]
sirkuit[0:5:2] = ["Naufal", "Rizky", "Rahman"]
print(sirkuit)

del sirkuit[3]
print(sirkuit)

sirkuit.remove("Marina Bay")
print(sirkuit)

namadihapus = sirkuit.pop(0)
print(namadihapus)

matkul_1 = ["Kalkulus", "logmat", "apd"]
matkul_2 = ["basis data", "apl", "pbo"]

matkul_gabungan = matkul_1 + matkul_2
print(matkul_gabungan)

matkul_1 = matkul_1 * 5
print(matkul_1)

line_up = [
    ["Ferrari", "Leclerc", 16],
    ["Mercedes", "Hamilton", 44],
    ["Red Bull", "Verstappen", 1],
    ["McLaren", "Norris", 4]
]

# print(line_up[2][1])

for i in line_up:
    for j in i:
        print(j)

chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
listchara = list(chara)

listchara.append("rawrrrrr")
print(listchara)

del listchara[6]
print(listchara)