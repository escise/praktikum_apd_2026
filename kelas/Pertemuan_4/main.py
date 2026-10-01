batas = 5
for i in range(batas):
    print("Perulangan Ke-", i)  


game = ["Genshin", 7.0, True]
for i in game:
    print(i)


for i in range(1, 3):
    for j in range(1, 4):
        print(f'{i} x {j} = {i * j}')
    print('')


jawab = "ya"
hitung = 0

while(jawab == "ya"):
    hitung += 1 
    jawab = input("Ulang lagi tidak? ")

print(f"Total Perulangan : {hitung}")


angka_benar = 7

while True:
    print("=== Game tebak angka ===")

    angka_input = int(input("Masukkan angka (1-10): "))

    if angka_benar == angka_input:
        print("Angka yang kamu masukkan benar")
        break
    else:
        print("Angka masih salah")


for i in range(10):
    if i % 2 == 0:
        continue
print(i)


uang_awal = int(input("masukkan uang saku awal kamu: "))

while uang_awal > 0:
    uang_kurang = int(input("masukkan nominal uang yang akan dikeluarkan: "))
    uang_awal -= uang_kurang
    print(f"uang sisa: ", uang_awal)
    
print("miskin")
