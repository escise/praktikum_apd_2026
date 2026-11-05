import inquirer

def menu_awal():
    m = [
        inquirer.List(
            'menu_awal',
            message = "Pilih Metode Login anda",
            choices = ['Register','Login','Keluar dari sistem']
            )
    ]

    i = inquirer.prompt(m)

    if i and 'menu_awal':
        return i['menu_awal']
    return None

def menu_utama():
    print('''=============== Selamat Datang ================''')
    mu = [ 
        inquirer.List(
            'menu_utama',
            choices=[
            '1. Buka List Stok Barang Elektronik',
            '2. Tambah Stok Barang Elektronik Baru (Admin)',
            '3. Update Stok Barang Elektronik (Admin)',
            '4. Hapus Stok Barang Elektronik (Admin)',
            '5. Total Stok Keseluruhan',
            '6. Keluar dari Program'
            ]
        )
    ]
        
    i = inquirer.prompt(mu)

    if i and 'menu_utama':
        return i['menu_utama']
    return None
    