import crud as c

def menu_utama():
    c.inisialisasi_db()
    
    while True:
        print("\n--- Aplikasi Manajemen Keuangan Perusahaan ---")
        print("1. Catat Pemasukan")
        print("2. Catat Pengeluaran")
        print("3. Lihat Semua Transaksi")
        print("4. Update Transaksi")
        print("5. Hapus Transaksi")
        print("6. Lihat Laporan Keuangan")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-7): ")
        df = c.baca_data()

        if pilihan == '1':
            kategori = input("Masukkan Kategori Pemasukan: ")
            while True:
                try:
                    jumlah = float(input("Masukkan Jumlah: "))
                    break
                except ValueError:
                    print("Input jumlah harus berupa angka.")
            deskripsi = input("Masukkan Deskripsi: ")
            df = c.tambah_transaksi(df, kategori, "Pemasukan", jumlah, deskripsi)
            c.tulis_data(df)
            print("Pemasukan berhasil dicatat.")

        elif pilihan == '2':
            kategori = input("Masukkan Kategori Pengeluaran: ")
            while True:
                try:
                    jumlah = float(input("Masukkan Jumlah: "))
                    break
                except ValueError:
                    print("Input jumlah harus berupa angka.")
            deskripsi = input("Masukkan Deskripsi: ")
            df = c.tambah_transaksi(df, kategori, "Pengeluaran", jumlah, deskripsi)
            c.tulis_data(df)
            print("Pengeluaran berhasil dicatat.")
        
        elif pilihan == '3':
            c.lihat_semua_transaksi(df)

        elif pilihan == '4':
            id_transaksi = int(input("Masukkan ID transaksi yang akan diupdate: "))
            kolom = input("Nama kolom yang akan diupdate (kategori/jumlah/deskripsi): ")
            if kolom in ['jumlah']:
                nilai_baru = float(input(f"Masukkan nilai baru untuk {kolom}: "))
            else:
                nilai_baru = input(f"Masukkan nilai baru untuk {kolom}: ")
            df = c.update_transaksi(df, id_transaksi, kolom, nilai_baru)
            c.tulis_data(df)

        elif pilihan == '5':
            id_transaksi = int(input("Masukkan ID transaksi yang akan dihapus: "))
            konfirmasi = input(f"Apakah Anda yakin ingin menghapus transaksi dengan ID {id_transaksi}? (y/n): ")
            if konfirmasi.lower() == 'y':
                df = c.hapus_transaksi(df, id_transaksi)
                c.tulis_data(df)
            else:
                print("Penghapusan dibatalkan.")

        elif pilihan == '6':
            c.buat_laporan(df)

        elif pilihan == '7':
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu_utama()