"""Fungsi untuk menyimpan dan membaca data pengeluaran."""

import os
from pengeluaran.models import Pengeluaran
from pengeluaran.validasi import (
    validasi_pengeluaran,
    DataTidakValidError,
)


FILE_DATA = "data/pengeluaran.txt"


def siapkan_folder():
    """Membuat folder data jika belum tersedia."""
    os.makedirs("data", exist_ok=True)
    os.makedirs("laporan", exist_ok=True)


def simpan_pengeluaran(pengeluaran):
    """Menyimpan satu data pengeluaran ke file."""
    siapkan_folder()
    validasi_pengeluaran(pengeluaran)

    # Mode a menambahkan data tanpa menghapus data sebelumnya.
    with open(FILE_DATA, "a", encoding="utf-8") as file:
        file.write(pengeluaran.ke_baris())


def baca_pengeluaran():
    """Membaca data dan melewati baris yang tidak valid."""
    siapkan_folder()
    daftar_pengeluaran = []

    # Mode x membuat file baru jika file belum ada.
    try:
        with open(FILE_DATA, "x", encoding="utf-8"):
            pass
    except FileExistsError:
        # File sudah tersedia, sehingga tidak perlu dibuat ulang.
        pass

    # Mode r digunakan untuk membaca isi file.
    try:
        with open(FILE_DATA, "r", encoding="utf-8") as file:
            for baris in file:
                if not baris.strip():
                    continue

                try:
                    pengeluaran = Pengeluaran.dari_baris(baris)
                    validasi_pengeluaran(pengeluaran)
                    daftar_pengeluaran.append(pengeluaran)
                except (ValueError, DataTidakValidError) as error:
                    print(f"Data dilewati karena tidak valid: {error}")

    except FileNotFoundError:
        print("File data belum ditemukan.")

    return daftar_pengeluaran


if __name__ == "__main__":
    # Menguji fungsi pembacaan data secara langsung.
    data = baca_pengeluaran()
    print(f"Jumlah data pengeluaran: {len(data)}")
