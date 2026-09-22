
harga_skincare = [
    35000,
    42000,
    50000,
    55000,
    68000,
    70000
]

ongkos_kirim_instan = 12000
nim = 56
kurs_jpy = 113

total_skincare = (
    harga_skincare[0]
    + harga_skincare[1]
    + harga_skincare[2]
    + harga_skincare[3]
    + harga_skincare[4]
    + harga_skincare[5]
)

total_pengeluaran = total_skincare + ongkos_kirim_instan
total_pengeluaran_kurs_jpy = total_pengeluaran / kurs_jpy

total_data = len(harga_skincare)
rata_rata = total_pengeluaran / total_data

bolean = nim < rata_rata

slice_negatif = harga_skincare[-4:-1]

print(harga_skincare)
print(ongkos_kirim_instan)
print(nim)
print(kurs_jpy)
print(total_skincare)
print(total_pengeluaran)
print(total_pengeluaran_kurs_jpy)
print(total_data)
print(rata_rata)
print(bolean)
print(slice_negatif)
