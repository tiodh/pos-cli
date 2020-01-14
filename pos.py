import csv
import os

# Input data dan load
# pencarian
# Penjualan
# Stok

while True:
    menu = ['1. Data Barang','2. Pencarian Barang', '3. Penjualan', '4. Stok']
    submenu1 = ['1. List Barang', '2. Input Barang', '3. Kembali']
    DATABASE_FILE = 'database.csv'
    database = []

    # Load data dari CSV
    with open(DATABASE_FILE) as db_file:
        csv_reader = csv.reader(db_file,delimiter=';')
        for row in csv_reader:
            database.append(row)
    id_barang = int(database[len(database)-1][0])+1
    os.system("clear")
    print('\t'.join(menu))
    aksi = input("Pilihan: ")
    os.system("clear")
    if aksi=='1':
        while True:
            print('\t'.join(submenu1))
            aksiMenu1 = input("Pilih: ")
            if aksiMenu1=='1':
                # Menampilkan data dari Array database
                print("\n%2s \t %10s \t %10s" %("ID","Nama","Harga"))
                for row in database:
                    print("%2s \t %10s \t %10s" %(row[0],row[1], row[2]))
                print("")
            elif aksiMenu1=='2':
                with open(DATABASE_FILE, mode='a') as db_file:
                    csv_writer = csv.writer(db_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    while True:
                        nama_barang = input('Masukkan Nama: ')
                        if nama_barang=='=':
                            break
                        harga_barang = input('Masukkan Harga: ')
                        csv_writer.writerow([id_barang, nama_barang, harga_barang])
                        database.append([id_barang, nama_barang, harga_barang])
                        id_barang += 1
                        os.system("clear")
                        print("Barang Telah Ditambahkan\n")
            elif aksiMenu1 == '3':
                break 
            else:
                print('salah input')    