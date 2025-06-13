import pandas as pd
import os

dataSudah = "data/data_sudah.csv"
dataHasil = "data/data_hasil.csv"
dataPetugas = "data/data_petugas.csv"
dataPeserta = "data/data_peserta.csv"
cekpetugas = os.path.exists(dataPetugas)
cekpeserta = os.path.exists(dataPeserta)
cekhasil = os.path.exists(dataHasil)
cekSudah = os.path.exists(dataSudah)

petugas =  pd.read_csv(dataPetugas)
peserta =  pd.read_csv(dataPeserta)
hasilVote =  pd.read_csv(dataHasil)
sudahVote =  pd.read_csv(dataSudah)

# if not cekSudah:
#     df = pd.DataFrame(columns=['Nama Siswa'])
#     df.to_csv(dataSudah, index=False)

# if not cekhasil:
#     df = pd.DataFrame(columns=['Nama Siswa'])
#     df.to_csv(dataHasil, index=False)

# if not cekpetugas:
#     df = pd.DataFrame(columns=['Nama Siswa'])
#     df.to_csv(dataPetugas, index=False)

# if not cekpeserta:
#     df = pd.DataFrame(columns=['Nama Siswa'])
#     df.to_csv(dataPeserta, index=False)

def verifyPetugas(usn, pw):
    akun = petugas[(petugas['Username'] == usn) & (petugas['Password'] == pw)]
    if akun.empty:
        return False
    else:
        return usn

def verify(nama, nis):
    peserta['NIS'] = peserta['NIS'].astype(str)
    akun = peserta[
        (peserta['Nama'].str.lower() == nama.lower()) &
        (peserta['NIS'] == str(nis))
    ]
    if akun.empty:
        return None
    else:
        return akun.iloc[0].to_dict()

def main():
    print(f"\n{"="*9} LOGIN UNTUK VERIFIKASI PETUGAS {"="*9}")
    while True:
        usn = input("Masukkan Username Anda : ")
        pw = input("Masukkan Password Anda : ")
        login = verifyPetugas(usn, pw)
        if login:
            print(f"SELAMAT {login} BERHASIL LOGIN")
            break
        else:
            print("NIK ATAU NAMA SALAH")
    print(f"\n{"="*12} SELAMAT DATANG DI PEMILU {"="*12}")
    print(f"\n{"-"*21}| Menu |{"-"*21}")
    print("-"*50)
    print("{:<0} {:<5} {:<0} {:<38} {:<0}".format("|","No","|", "Pilihan", "|"))
    print("-"*50)
    print("{:<0} {:<5} {:<0} {:<38} {:<0}".format("|","1","|", "Memulai Vote", "|"))
    print("{:<0} {:<5} {:<0} {:<38} {:<0}".format("|","2","|", "Hasil Pemilu", "|"))
    print("{:<0} {:<5} {:<0} {:<38} {:<0}".format("|","3","|", "Exit", "|"))
    print("-"*50)
    while True:
        pilihan = input("Pilih Menu : ")
        if pilihan == "1":
            while True:
                print(f"{'='*9}SELAMAT DATANG PESERTA PILKETOS{'='*10}")
                print("SILAHKAN VERIFIKASI KAN DIRI ANDA")
                nama = input("Masukkan Nama Anda : ")
                nis = int(input("Masukkan NIS Anda : "))
                login = verify(nama, nis)
                if login is not None:
                    print("SELAMAT ANDA BERHASIL LOGIN")
                    kelas = login['Kelas']
                    print("Kelas Anda:", kelas)
                    break
                else:
                    print("NAMA ATAU NIS SALAH")
main()