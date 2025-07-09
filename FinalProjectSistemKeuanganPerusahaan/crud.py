import pandas as pd
import os
from datetime import datetime

nama_file = 'database_keuangan.csv'
kolom = ['id', 'tanggal', 'kategori', 'jenis', 'jumlah', 'deskripsi']

def inisialisasi_db():
    if not os.path.exists(nama_file):
        df = pd.DataFrame(columns=kolom)
        df.to_csv(nama_file, index=False)

def baca_data():
    try:
        df = pd.read_csv(nama_file)
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=kolom)

def tulis_data(df):
    df.to_csv(nama_file, index=False)

def tambah_transaksi(df, kategori, jenis, jumlah, deskripsi):
    id_baru = df['id'].max() + 1 if not df.empty else 1
    tanggal_hari_ini = datetime.now().strftime('%Y-%m-%d')
    
    data_baru = pd.DataFrame([{
        'id': id_baru,
        'tanggal': tanggal_hari_ini,
        'kategori': kategori,
        'jenis': jenis,
        'jumlah': jumlah,
        'deskripsi': deskripsi
    }])
    
    df_updated = pd.concat([df, data_baru], ignore_index=True)
    return df_updated

def lihat_semua_transaksi(df):
    if df.empty:
        print("Belum ada data transaksi.")
    else:
        print(df.to_string())

def update_transaksi(df, id_transaksi, kolom_update, nilai_baru):
    if id_transaksi not in df['id'].values:
        print(f"Error: ID {id_transaksi} tidak ditemukan.")
        return df

    kolom_valid = ['kategori', 'jumlah', 'deskripsi']
    if kolom_update not in kolom_valid:
        print(f"Error: Kolom '{kolom_update}' tidak valid. Kolom yang dapat diupdate: {kolom_valid}")
        return df

    df.loc[df['id'] == id_transaksi, kolom_update] = nilai_baru
    print(f"Data dengan ID {id_transaksi} berhasil diperbarui.")
    return df

def hapus_transaksi(df, id_transaksi):
    if id_transaksi not in df['id'].values:
        print(f"Error: ID {id_transaksi} tidak ditemukan.")
        return df
        
    df = df[df['id'] != id_transaksi]
    print(f"Data dengan ID {id_transaksi} berhasil dihapus.")
    return df.reset_index(drop=True)

def buat_laporan(df):
    if df.empty:
        print("Tidak ada data untuk membuat laporan.")
        return

    df['tanggal'] = pd.to_datetime(df['tanggal'])
    df['bulan'] = df['tanggal'].dt.to_period('M')
    df['tahun'] = df['tanggal'].dt.to_period('Y')

    print("\n--- LAPORAN BULANAN ---")
    laporan_bulanan = df.groupby(['bulan', 'jenis'])['jumlah'].sum().unstack(fill_value=0)
    print(laporan_bulanan)
    
    print("\n--- LAPORAN TAHUNAN ---")
    laporan_tahunan = df.groupby(['tahun', 'jenis'])['jumlah'].sum().unstack(fill_value=0)
    print(laporan_tahunan)