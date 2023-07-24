import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Daftar Pesanan")
    print("Barang yang dibeli : ")
    for item in pesanan:
        print("[", item, "]")
    print("Harga Pesanan :")
    for harga in harga_pesanan:
        print("Rp.", harga)

menu= { 
    "Pandan Latte": 28000,
    "Matcha": 29000,
    "Espresso":25000,
    "Cuppuchino":28000,
    "Kopi Kenangan Mantan": 31000,
    "Kopi Kangen":26000,
    "Kopi Enak": 18000
}


pesanan = [] #array untuk simpan nama menu yang dipesan
harga_pesanan = [] #array untuk simpan harga menu yang dipesan
lanjut = True

while lanjut :
    clear_terminal()
    print("Selamat Datang di KoPhy!!")
    print("==================================")
    print("Daftar Menu pada Warung Kopi Kita")
    for nama,harga in menu.items(): #tampilkan daftar menu dengan looping for
        print(nama, "Rp.", harga)

    print("Daftar Pesanan")
    pilihKopi = int(input("Masukkan Kode Menu : "))
    pilihkopi1 = pilihKopi-1;
    pesanan.append(list(menu.keys())[pilihkopi1]) # Menambahkan nama menu yang dipilih ke dalam list pesanan
    harga_pesanan.append(menu[list(menu.keys())[int(pilihkopi1)]])  # Menambahkan harga pesanan ke dalam list

    pilihan_lanjut = input("Lanjutkan pemesanan? (y/t): ")
    if(pilihan_lanjut != "y"):
        lanjut = False

os.system('cls' if os.name == 'nt' else 'clear')    
print("Daftar Pesanan")
print("==================================")
print("Barang yang dibeli : ")
for item in pesanan:
    print("[", item, "]")
print("Harga Pesanan :")
for harga in harga_pesanan:
    print("Rp.", harga)
total_harga = sum(harga_pesanan)
print("Total Harga yang harus dibayarkan : ", total_harga)       

kurang=True
while kurang:
    uangbayar = int(input("Masukkan Uang Pembayaran : "))
    if(uangbayar<total_harga):
        print("Maaf, Uang anda kurang!! Silahkan masukkan kembali!")
        kurang = True
    elif(uangbayar>total_harga):
        kurang=False
        kembalian = uangbayar - total_harga
        print("Kembalian : ",kembalian)

