def verify(nama,  nik):
    dataPeserta = dataPeserta()
    if nama in dataPeserta and dataPeserta[nama] == nik:
        return True
    else:
        return False
    
def dataPeserta():
    peserta = {
        "jhon" : "1234",
        "jane" : "5678",
        "jack" : "9012"        
    }
    return peserta

def dataPetugas():
    petugas = {
        "admin" : "admin123",
        "petugas" : "petugas123"
        }
    return petugas

def verifyPetugas(usn, pw):
    data = dataPetugas()
    if usn in data and data[usn] == pw:
        return True
    else:
        return False

def petugas():
    while True:
        print("SELAMAT DATANG PETUGAS PANITIA PEMILU")
        print("SILAHKAN VERIFIKASI KAN DIRI ANDA")
        usn = input("Masukkan Username Anda : ")
        pw = input("Masukkan Password Anda : ")
        verify = verifyPetugas(usn, pw)
        if verify:
            print("SELAMAT ANDA BERHASIL LOGIN")
            break
        else:
            print("USERNAME ATAU PASSWORD SALAH")