daftarKontak =[
    {   'Index': '01',
        'Nama perusahaan' : 'PT.Maju Mundur',
        'Lokasi' : 'Bekasi',
        'Nomor pokok perusahaan' : '000123',
        'Nomor telepon' : '021345689'
    },
    {   'Index': '02',
        'Nama perusahaan' : 'PT.Sejahtera',
        'Lokasi' : 'Tangerang',
        'Nomor pokok perusahaan' : '000345',
        'Nomor telepon' : '021278891'
    },
    {  'Index': '03',
        'Nama perusahaan' : 'PT.XYZ',
        'Lokasi' : 'Depok',
        'Nomor pokok perusahaan' : '000456',
        'Nomor telepon' : '021567234' 
    },
    {  'Index': '04',
        'Nama perusahaan' : 'PT.Intan',
        'Lokasi' : 'Bogor',
        'Nomor pokok perusahaan' : '000567',
        'Nomor telepon' : '021784563' 
    },
    {   'Index': '05',
        'Nama perusahaan' : 'PT.Adi Karya',
        'Lokasi' : 'Cimahi',
        'Nomor pokok perusahaan' : '000678',
        'Nomor telepon' : '021869577'
    }
]

#MENU UTAMA
def menuUtama():
    while true:
        pilihan_menu = input ('''
        List Menu :
        1. Menampilkan Daftar Kontak Perusahaan 
        2. Menambah Data Kontak Perusahaan 
        3. Mengupdate Data Kontak Perusahaan 
        4. Menghapus Data Kontak Perusahaan 
        5. Exit Program
    
        Masukkan nomor yang dipilih: ''')
        
    if (pilihanMenu == '1') :
        MenampilkanDaftarKontakPerusahaan()
    elif (pilihanMenu == '2') :
        MenambahkanDataKontak()
    elif (pilihanMenu == '3') :
        MengupdateDataKontak()
    elif (pilihanMenu == '4') :
        MenghapusDataKontak()
    elif (pilihanMenu == '5') :
        ExitProgram()
    else :
        print ('pilihan yang anda masukkan salah, silahkan pilih menu yang tersedia')
        Continue 

#MENU 1. MENAMPILKAN DAFTAR KONTAK PERUSAHAAN / MENU READ DATA
def MenampilkanDaftarKontakPerusahaan():
    while True :
        menu = input ('''
        List Menu :
        1. Menampilkan semua daftar kontak perusahaan
        2. Menampilkan daftar berdasarkan prime key : nomor pokok perusahaan
        3. Kembali ke menu utama 
    
        Masukkan menu yang dipilih: ''')
        
    if Menu == '1':
        if len(daftarKontak)!=0:
            MenampilkanSeluruhData()
        else:
            print ("Tidak ada data")
    elif Menu == '2':
        nomorPokokPerusahaan = input ("Masukkan nomor pokok perusahaan yang dicari: ")
        for i in range(len(daftarKontak)):
            if nomorPokokPerusahaan == daftarKontak[i]['Nomor pokok perusahaan']:
                print ('Daftar kontak perusahaan: \n Index \t | Nama Perusahaan \t\t | Lokasi \t | Nomor Pokok Perusahaan \t | Nomor Telepon \t')
                print ('{} \t | {} \t | {} \t | {} \t | {}'.format(i, daftarKontak[i]['Index'], daftarKontak[i]['Nama perusahaan'], daftarKontak[i]['Lokasi'], daftarKontak[i]['Nomor pokok perusahaan'], daftarKontak[i]['Telepon']))
            else:
                print ("Tidak ada data")
                break
    elif Menu == '3':
        break

    else :
        print ('pilihan yang anda masukkan salah, silahkan pilih menu yang tersedia')
        continue

def MenampilkanSeluruhData():
    print ('Daftar kontak perusahaan: \n Index \t | Nama Perusahaan \t\t | Lokasi \t | Nomor Pokok Perusahaan \t | Nomor Telepon \t')
    for i in range (len(daftarKontak)):
        print ('{} \t | {} \t | {} \t | {} \t | {}'.format(i, daftarKontak[i]['Index'], daftarKontak[i]['Nama perusahaan'], daftarKontak[i]['Lokasi'], daftarKontak[i]['Nomor pokok perusahaan'], daftarKontak[i]['Telepon']))
        break

#MENU 2. Menambah Data Kontak Perusahaan / MENU CREATE DATA
def MenambahDataKontak():
    MenampilkanSeluruhData() 
    while True :
        menu = input('''
        List Menu :
        1. Menambah kontak perusahaan
        2. Kembali ke menu utama 
        
        Masukkan menu yang anda pilih: ''')
        
    if Menu == '1':
        nomorPokokPerusahaan = input ("Masukkan nomor pokok perusahaan: ")
        for i in range (len(daftarKontak)):
            print (i)
            print (nomorPokokPerusahaan)
            print (daftarKontak)
            if nomorPokokPerusahaan == daftarKontak[i]['Nomor pokok perusahaan']:
                print ("Data sudah ada")
                MenambahDataKontak() 
                break 
            else:
                index = input ("Masukkan nomor index: ")
                namaPerusahaan = input ("masukkan nama perusahaan: ")
                lokasi = input ("Masukkan lokasi: ")
                nomorPokokPerusahaan = input ("Masukkan nomor pokok perusahaan: ")
                nomorTelepon = input ("Masukkan nomor telepon: ")
                cek = input ("Apakah anda akan menyimpan data? (Y/N): ") 
                if cek == 'Y':
                    daftarKontak.append(
                        {'Index' : 'Index',
                         'Nama perusahaan' : 'Nama perusahaan',
                         'Lokasi': 'Lokasi',
                         'Nomor pokok perusahaan': 'Nomor pokok perusahaan',
                         'Nomor telepon': 'Nomor telepon'})
                    print ("Data tersimpan")
                    break 
                elif cek == 'N':
                    print ("Data tidak disimpan")
                    break 
                else :
                    cek = input ("Apakah anda akan menyimpan data? (Y/N): ") 
                    continue 

            MenampilkanSeluruhData() 
            break 
    elif Menu == '2':
        for i in range(len(daftarKontak)):
            break 
    else :
        for i in range(len(daftarKontak)):
            print ("Pilihan yang anda masukkan salah, silahkan pilih menu yang tersedia")
            continue

#MENU 3. Mengupdate Data Kontak Perusahaan / MENU UPDATE DATA
def mengupdateKontak():
    MenampilkanSeluruhData() 
    while True :
        menu = input('''
        List Menu :
        1. Mengupdate data kontak perusahaan
        2. Kembali ke menu utama
        
        Masukkan menu yang anda pilih: ''')
    
    if Menu == '1':
        nomorPokokPerusahaanUpdate = input ("Masukkan nomor pokok perusahaan yang ingin diupdate: ")
        for i in range (len(daftarKontak)):
            if nomorPokokPerusahaan == daftarKontak[i]['Nomor pokok perusahaan']: 
                update = input ("Masukkan bagian yang ingin diupdate: ")
            if update == 'Nama perusahaan':
                namaPerusahaanUpdate = input ("Masukkan nama perusahaan terbaru: ").capitalize()
                cek = input ("Apakah anda akan menyimpan data? (Y/N): ").upper() 
                if cek == 'Y' :
                    daftarKontak[i][update] = namaPerusahaanUpdate 
                    print ("Data terupdate") 
                    break 
                else:
                    print ("Data tidak tersimpan")
                    break
            elif update == 'Lokasi':
                lokasiUpdate = input ("Masukkan lokasi perusahaan terbaru: ").capitalize()
                cek = input ("Apakah anda akan menyimpan data? (Y/N): ").upper() 
                if cek == 'Y' :
                    daftarKontak[i][update] = lokasiUpdate 
                    print ("Data terupdate") 
                    break 
                else:
                    print ("Data tidak tersimpan")
                    break 
            elif update == 'Nomor telepon':
                nomorTeleponUpdate = input ("Masukkan nomor telepon perusahaan terbaru: ").capitalize()
                cek = input ("Apakah anda akan menyimpan data? (Y/N): ").upper() 
                if cek == 'Y' :
                    daftarKontak[i][update] = nomorTeleponUpdate 
                    print ("Data terupdate") 
                    break 
                else:
                    print ("Data tidak tersimpan")
                    break
            else: 
                print ("Data yang anda cari tidak ada")
                print ("Masukkan menu yang anda pilih")
                continue

    elif Menu == '2':
        break 
    else: 
        print ("Pilihan yang anda masukkan salah, silahkan pilih menu yang tersedia")
        continue               

#MENU 4. Menghapus Data Kontak Perusahaan / MENU DELETE DATA
def menghapusKontak():
    MenampilkanSeluruhData() 
    while True :
        menu = input ('''
        List Menu :
        1. Menghapus data kontak perusahaan
        2. Kembali ke menu utama
        
        Masukkan menu yang anda pilih: ''')
       
    if Menu == '1':
        indexTerhapus = input ("Masukkan bagian yang akan dihapus: ")
        for i in range (len(daftarKontak)):
            if indexTerhapus == daftarKontak[i]['Index']: 
                del daftarKontak [i][index]
                cek = input ("Apakah anda akan menyimpan data? (Y/N): ").upper() 
                if cek == 'Y' :
                    daftarKontak [i][indexTerhapus] = indexTerhapus 
                    print ("Data deleted") 
                    break 
                else:
                    print ("Data tidak tersimpan")
            else:
                print ("Data yang anda cari tidak ada")
                print ("Masukkan menu yang anda pilih")
                continue

    elif Menu == '2':
        break 
    else: 
        print ("Pilihan yang anda masukkan salah, silahkan pilih menu yang tersedia")
        continue                             
 
#MENU 5. EXIT PROGRAM 
def ExitProgram():
    MenampilkanSeluruhData() 
    while True :
        menu = input ('''
        1. Kembali ke menu utama
        
        Masukkan menu yang anda pilih: ''')
    break 