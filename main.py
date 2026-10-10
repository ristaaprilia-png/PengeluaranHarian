"""Program utama pencatatan pengeluaran harian."""

from pengeluaran.models import Pengeluaran
from pengeluaran.fileio import (
    simpan_pengeluaran,
    baca_pengeluaran,
)
from pengeluaran.processing import (
    hitung_total,
    urutkan_pengeluaran,
)
from pengeluaran.laporan import (
    buat_laporan,
    simpan_laporan,
)
from pengeluaran.validasi import DataTidakValidError


def tambah_data():
    """Meminta pengguna memasukkan data pengeluaran."""
    try:
        tanggal = input("Tanggal (DD-MM-YYYY): ").strip()
        kategori = input("Kategori: ").strip()
        keterangan = input("Keterangan: ").strip()
        nominal = int(input("Nominal (Rp): "))

        data = Pengeluaran(
            tanggal=tanggal,
            kategori=kategori,
            keterangan=keterangan,
            nominal=nominal,
        )

        simpan_pengeluaran(data)
        print("Data pengeluaran berhasil disimpan.")

    except ValueError:
        print("Nominal harus berupa bilangan bulat.")

    except DataTidakValidError as error:
        print(f"Data tidak valid: {error}")


def tampilkan_data():
    """Menampilkan seluruh data pengeluaran."""
    data = baca_pengeluaran()

    if not data:
        print("Belum ada data pengeluaran.")
        return

# Mengurutkan data dari nominal terbesar ke terkecil.
    data_urut = urutkan_pengeluaran(data, urutan="terbesar")

    print("\n===== DAFTAR PENGELUARAN =====")
    for nomor, item in enumerate(data_urut, start=1):
        print(
            f"{nomor}. {item.tanggal} | {item.kategori} | "
            f"{item.keterangan} | Rp{item.nominal:,}".replace(",", ".")
        )

    print(
        f"Total pengeluaran: Rp{hitung_total(data):,}".replace(",", ".")
    )


def tampilkan_laporan():
    """Membuat, menampilkan, dan menyimpan laporan."""
    data = baca_pengeluaran()

    if not data:
        print("Belum ada data untuk dibuat laporan.")
        return

# Mengolah data menjadi laporan, lalu menampilkan dan menyimpannya.
    isi = buat_laporan(data)
    print("\n" + isi)

    simpan_laporan(isi)
    print("\nLaporan berhasil disimpan.")


def main():
    """Menampilkan menu utama program."""
    while True:
        print("\n===== PENCATATAN PENGELUARAN HARIAN =====")
        print("1. Tambah pengeluaran")
        print("2. Lihat daftar pengeluaran")
        print("3. Buat laporan")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            tampilkan_laporan()
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1-4.")


if __name__ == "__main__":
    main()
