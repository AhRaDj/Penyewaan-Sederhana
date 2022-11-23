import os

Pesawat = []
pesawatBekas = []
pesawatBeli = []
pesawatSewa1 = []
pesawatSewa2 = []

def halamanLogin():
    os.system('cls')
    print("====== Aplikasi Penyewaan Pesawat ======\n")
    print("1. Admin")
    print("2. User 1")
    print("3. User 2")
    pilihLogin = int(input("\nLogin Sebagai : "))
    login(pilihLogin)

def halamanAdmin():
    print("====== Aplikasi Penyewaan Pesawat ======\n")
    print("Selamat Datang Admin\n")
    print("1. Input Pesawat")
    print("2. Hapus Pesawat")
    print("3. Daftar Pesawat")
    print("4. Daftar Penjualan")
    print("5. Back")
    pilihAdmin = int(input("\nPilih Menu : "))
    menuAdmin(pilihAdmin)

def halamanUser(user):
    os.system('cls')
    if(user == 2):
        print("Selamat Datang User 1\n")
    elif(user == 3):
        print("Selamat Datang User 2\n")
    print("1. Pembeli")
    print("2. Penyewa")
    print("3. Back")
    pilihUser = int(input("\nMasuk Sebagai : "))
    menuUser(user, pilihUser)

def halamanBeli(user):
    os.system('cls')
    print("====== Aplikasi Pembelian Pesawat ======\n")
    if(user == 2):
        print("Selamat Datang User 1\n")
    elif(user == 3):
        print("Selamat Datang User 2\n")
    print("1. Pesawat Baru")
    print("2. Pesawat Bekas")
    print("3. Kembali\n")
    pilihBeli = int(input("\nPilih Menu : "))
    menuBeli(user, pilihBeli)

def halamanSewa(user):
    os.system('cls')
    print("====== Aplikasi Penyewaan Pesawat ======\n")
    if(user == 2):
        print("Selamat Datang User 1\n")
    elif(user == 3):
        print("Selamat Datang User 2\n")
    print("1. Penyewaan")
    print("2. Pengembalian")
    print("3. Status")
    print("4. Daftar Pesawat")
    print("5. Kembali\n")
    pilihSewa = int(input("\nPilih Menu : "))
    menuSewa(user, pilihSewa)

def halamanSewaPilih(user):
    os.system('cls')
    print("====== Aplikasi Penyewaan Pesawat ======\n")
    if(user == 2):
        print("Selamat Datang User 1\n")
    elif(user == 3):
        print("Selamat Datang User 2\n")
    print("1. Pesawat Baru")
    print("2. Pesawat Bekas")
    print("3. Kembali\n")
    pilihPesawat = int(input("\nPilih Menu : "))
    pilihSewa(user, pilihPesawat)

def listPesawat(user):
    print("\nPesawat Baru:")
    for i in range(len(Pesawat)):
        print(str(i+1) + ". "+ Pesawat[i])
    print("\nPesawat Bekas:")
    for i in range(len(pesawatBekas)):
        print(str(i+1) + ". "+ pesawatBekas[i])
    back = input("Ingin Kembali? (y/t): ")
    if (back == "y"):
        if (user == 1):
            os.system('CLS')
            halamanAdmin()
        elif(user == 2 or user == 3):
            os.system('CLS')
            halamanSewa(user)
    elif(back == "t"):
            halamanLogin()
    
def listPenjualan():
    print("\nPesawat yang Telah Dijual:")
    for i in range(len(pesawatBeli)):
        print(str(i+1) + ". "+ pesawatBeli[i])
    back = input("Press any to continue")
    halamanLogin()

def login(pilih):
    if pilih == 1:
        os.system('cls')
        halamanAdmin()
    elif pilih == 2:
        os.system('cls')
        halamanUser(pilih)
    elif pilih == 3:
        os.system('cls')
        halamanUser(pilih)
    else:
        print("Pilihan Tidak Tersedia")

def menuAdmin(pilih):
    if pilih == 1:
        Lanjut = True
        while(Lanjut):
            Pesawat_baru = input("Tambahkan Pesawat: ")
            inputPesawat(Pesawat_baru)
            tambah = input("Ingin Menambahkan? (y/t): ")
            if(tambah == "t"): 
                Lanjut = False
        os.system('cls')
        halamanAdmin()
        
    elif pilih == 2:
        if len(Pesawat) == 0:
            print("Pesawat Tidak Tesedia")
            back = input("Ingin Kembali? (y/t): ")
            if(back == "y"):
                os.system('CLS')
                halamanAdmin()
            elif(back == "t"):
                halamanLogin()
        else:
            print("Daftar Pesawat : ")
            for i in range(len(Pesawat)):
                print(str(i+1) + ". "+ Pesawat[i])
            pilihHapus = int(input("Pilih Pesawat: ")) - 1
            deletePesawat(pilihHapus)

    elif pilih == 3:
        listPesawat(1)
    
    elif pilih == 4:
        listPenjualan()

    elif pilih == 5:
        halamanLogin()

    else:
        print("Pilihan Tidak Tersedia")
        halamanAdmin()

def inputPesawat(Pesawat_baru):
    Pesawat.append(Pesawat_baru)

def deletePesawat(pilihHapus):
    if pilihHapus + 1 > len(Pesawat):
        print("Pesawat Tidak Ada")
        back = input("Ingin Kembali? (y/t): ")
        if(back == "y"):
            os.system('CLS')
            halamanAdmin()
        elif(back == "t"):
            halamanLogin()
    else:
        for i in range(len(Pesawat)):
            if pilihHapus == i:
                del Pesawat[pilihHapus]
                os.system('CLS')
                halamanAdmin()

def menuUser(user, pilihUser):
    if pilihUser == 1:
        halamanBeli(user)
    elif pilihUser == 2:
        halamanSewa(user)
    elif pilihUser == 3:
        halamanLogin()
    else:
        os.system('cls')
        print("Pilihan Tidak Tersedia")
        halamanUser()

def menuBeli(user,pilihBeli):
    if pilihBeli == 1:
        beliBaru(user)
    elif pilihBeli == 2:
        beliBekas(user)
    elif pilihBeli == 3:
        os.system('cls')
        halamanUser(user)
    else:
        os.system('cls')
        print("Pilihan Tidak Tersedia")
        halamanUser(user)

def menuSewa(user, pilihSewa):
    if pilihSewa == 1:
        halamanSewaPilih(user)
    elif pilihSewa == 2:
        returnPesawat(user)
    elif pilihSewa == 3:
        statusSewa(user)
    elif pilihSewa == 4:
        listPesawat(user)
    elif pilihSewa == 5:
        os.system('cls')
        halamanUser(user)
    else:
        os.system('cls')
        print("Pilihan Tidak Tersedia")
        halamanUser(user)

def pilihSewa(user, pilihPesawat):
    if pilihPesawat == 1:
        sewaBaru(user)
    elif pilihPesawat == 2:
        sewaBekas(user)
    elif pilihPesawat == 3:
        os.system('cls')
        halamanUser(user)
    else:
        print("Pilihan Tidak Tersedia")

def beliBaru(user):
    if len(Pesawat) == 0:
        print("Pesawat Tidak Tesedia")
        back = input("Ingin Kembali? (y/t): ")
        if(back == "y"):
            os.system('CLS')
            halamanUser(user)
        elif(back == "t"):
            halamanLogin()
    else:
        print("\nPesawat yang Tersedia:")
        for i in range(len(Pesawat)):
            print(str(i+1) + ". "+ Pesawat[i])
        pilihUser = int(input("Pilih Pesawat: "))-1
        if(pilihUser+1 > len(Pesawat)):
            print("Pesawat Tidak Ditemukan")
            back = input("Ingin Kembali? (y/t): ")
            if(back == "y"):
                os.system('CLS')
                halamanUser(user)
            elif(back == "t"):
                halamanLogin()
        else:
            for i in range(len(Pesawat)):
                if(pilihUser == i):
                    pesawatBeli.append(Pesawat[pilihUser])
                    del Pesawat[pilihUser]
                    os.system('CLS')
                    halamanUser(user)

def beliBekas(user):
    if len(pesawatBekas) == 0:
        print("Pesawat Tidak Tesedia")
        back = input("Ingin Kembali? (y/t): ")
        if(back == "y"):
            os.system('CLS')
            halamanUser(user)
        elif(back == "t"):
            halamanLogin()
    else:
        print("\nPesawat Bekas yang Tersedia:")
        for i in range(len(pesawatBekas)):
            print(str(i+1) + ". "+ pesawatBekas[i])
        pilihUser = int(input("Pilih Pesawat: "))-1
        if(pilihUser+1 > len(pesawatBekas)):
            print("Pesawat Tidak Ditemukan")
            back = input("Ingin Kembali? (y/t): ")
            if(back == "y"):
                os.system('CLS')
                halamanBeli(user)
            elif(back == "t"):
                halamanLogin()
        else:
            for i in range(len(pesawatBekas)):
                if(pilihUser == i):
                    pesawatBeli.append(pesawatBekas[pilihUser])
                    del pesawatBekas[pilihUser]
                    os.system('CLS')
                    halamanBeli(user)

def sewaBaru(user):
    if len(Pesawat) == 0:
        print("Pesawat Tidak Tesedia")
        back = input("Ingin Kembali? (y/t): ")
        if(back == "y"):
            os.system('CLS')
            halamanSewa(user)
        elif(back == "t"):
            halamanLogin()
    else:
        print("\nPesawat yang Tersedia:")
        for i in range(len(Pesawat)):
            print(str(i+1) + ". "+ Pesawat[i])
        pilihUser = int(input("Pilih Pesawat: "))-1
        if(pilihUser+1 > len(Pesawat)):
            print("Pesawat Tidak Ditemukan")
            back = input("Ingin Kembali? (y/t): ")
            if(back == "y"):
                os.system('CLS')
                halamanSewa(user)
            elif(back == "t"):
                halamanLogin()
        else:
            for i in range(len(Pesawat)):
                if(pilihUser == i):
                    if (user == 2):
                        pesawatSewa1.append(Pesawat[pilihUser])
                    elif (user == 3):
                        pesawatSewa2.append(Pesawat[pilihUser])
                    del Pesawat[pilihUser]
                    os.system('CLS')
                    halamanSewa(user)

def sewaBekas(user):
    if len(pesawatBekas) == 0:
        print("Pesawat Tidak Tesedia")
        back = input("Ingin Kembali? (y/t): ")
        if(back == "y"):
            os.system('CLS')
            halamanSewa(user)
        elif(back == "t"):
            halamanLogin()
    else:
        print("\nPesawat yang Tersedia:")
        for i in range(len(pesawatBekas)):
            print(str(i+1) + ". "+ pesawatBekas[i])
        pilihUser = int(input("Pilih Pesawat: "))-1
        if(pilihUser+1 > len(pesawatBekas)):
            print("Pesawat Tidak Ditemukan")
            back = input("Ingin Kembali? (y/t): ")
            if(back == "y"):
                os.system('CLS')
                halamanSewa(user)
            elif(back == "t"):
                halamanLogin()
        else:
            for i in range(len(pesawatBekas)):
                if(pilihUser == i):
                    if (user == 2):
                        pesawatSewa1.append(pesawatBekas[pilihUser])
                    elif (user == 3):
                        pesawatSewa2.append(pesawatBekas[pilihUser])
                    del pesawatBekas[pilihUser]
                    os.system('CLS')
                    halamanSewa(user)

def returnPesawat(user):
    if (user == 2):
        if len(pesawatSewa1) == 0:
            print("Pesawat Tidak Tesedia")
            back = input("Ingin Kembali? (y/t): ")
            if(back == "y"):
                os.system('CLS')
                halamanSewa(user)
            elif(back == "t"):
                halamanLogin()
        else:
            print("\nNama : User 1")
            print("Pesawat Disewa : ")
            for i in range(len(pesawatSewa1)):
                print(str(i+1) + ". "+ pesawatSewa1[i])
            pilihUser = int(input("Pilih Pesawat: ")) - 1
            if(pilihUser+1 > len(pesawatSewa1)):
                print("Pesawat Tidak Ditemukan")
                back = input("Ingin Kembali? (y/t): ")
                if(back == "y"):
                    os.system('CLS')
                    halamanSewa(user)
                elif(back == "t"):
                    halamanLogin()
            else:
                for i in range(len(pesawatSewa1)):
                    if(pilihUser == i):
                        pesawatBekas.append(pesawatSewa1[pilihUser])
                        del pesawatSewa1[pilihUser]
                        os.system('CLS')
                        halamanSewa(user)

    elif (user == 3):
        if len(pesawatSewa2) == 0:
            print("Pesawat Tidak Tesedia")
            back = input("Ingin Kembali? (y/t): ")
            if(back == "y"):
                os.system('CLS')
                halamanSewa(user)
            elif(back == "t"):
                halamanLogin()
        else:
            print("\nNama : User 2")
            print("Pesawat Disewa : ")
            for i in range(len(pesawatSewa2)):
                print(str(i+1) + ". "+ pesawatSewa2[i])
            pilihUser = int(input("Pilih Pesawat: ")) - 1
            if(pilihUser+1 > len(pesawatSewa2)):
                print("Pesawat Tidak Ditemukan")
                back = input("Ingin Kembali? (y/t): ")
                if(back == "y"):
                    os.system('CLS')
                    halamanSewa(user)
                elif(back == "t"):
                    halamanLogin()
            else:
                for i in range(len(pesawatSewa2)):
                    if(pilihUser == i):
                        pesawatBekas.append(pesawatSewa2[pilihUser])
                        del pesawatSewa2[pilihUser]
                        os.system('CLS')
                        halamanSewa(user)

def statusSewa(user):
    if (user == 2):
        if len(pesawatSewa1) == 0:
            print("Belum Ada Pesawat yang Disewa")
            back = input("Ingin Kembali? (y/t): ")
            if(back == "y"):
                os.system('CLS')
                halamanSewa(user)
            elif(back == "t"):
                halamanLogin()
        else:
            print("\nPesawat Disewa : ")
            for i in range(len(pesawatSewa1)):
                print(str(i+1) + ". "+ pesawatSewa1[i])
            back = input("Ingin Kembali? (y/t): ")
            if(back == "y"):
                os.system('CLS')
                halamanSewa(user)
            elif(back == "t"):
                halamanLogin()

    elif (user == 3):
        if len(pesawatSewa2) == 0:
            print("Belum Ada Pesawat yang Disewa")
            back = input("Ingin Kembali? (y/t): ")
            if(back == "y"):
                os.system('CLS')
                halamanSewa(user)
            elif(back == "t"):
                halamanLogin()
        else:
            print("\nPesawat Disewa : ")
            for i in range(len(pesawatSewa2)):
                print(str(i+1) + ". "+ pesawatSewa2[i])
            back = input("Ingin Kembali? (y/t): ")
            if(back == "y"):
                os.system('CLS')
                halamanSewa(user)
            elif(back == "t"):
                halamanLogin()

halamanLogin()