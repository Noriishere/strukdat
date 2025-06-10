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

def verify(nik, password):
    data = dataPeserta()
    if nik in data and data[nik] == password:
        return True
    else:
        return False

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
            
def peserta():
    while True:
        print("SELAMAT DATANG PESERTA PEMILU")
        print("SILAHKAN VERIFIKASI KAN DIRI ANDA")
        nama = input("Masukkan NIK Anda : ")
        nik = input("Masukkan Password Anda : ")
        login = verify(nama, nik)
        if login:
            print("SELAMAT ANDA BERHASIL LOGIN")
            break
        else:
            print("NIK ATAU NAMA SALAH")

def main():
    print(f"\n{"="*9} LOGIN UNTUK VERIFIKASI PETUGAS {"="*9}")
    
    
    print(f"\n{"="*12} SELAMAT DATANG DI PEMILU {"="*12}")
    print(f"\n{"-"*21}| Menu |{"-"*21}")
    print("-"*50)
    print("{:<0} {:<5} {:<0} {:<38} {:<0}".format("|","No","|", "Pilihan", "|"))
    print("-"*50)
    print("{:<0} {:<5} {:<0} {:<38} {:<0}".format("|","1","|", "Vote", "|"))
    print("{:<0} {:<5} {:<0} {:<38} {:<0}".format("|","2","|", "Exit", "|"))
    print("-"*50)
main()