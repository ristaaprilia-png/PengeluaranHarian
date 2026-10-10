"""Fungsi untuk membuat laporan pengeluaran harian."""

from pengeluaran.processing import (
    hitung_total,
    hitung_rata_rata,
    kelompokkan_kategori,
    pengeluaran_terbesar,
)

FILE_LAPORAN = "laporan/laporan_pengeluaran.txt"


def buat_laporan(data):
    """Membuat isi laporan berdasarkan data pengeluaran."""

    total = hitung_total(data)
    rata_rata = hitung_rata_rata(data)
    kategori = kelompokkan_kategori(data)
    terbesar = pengeluaran_terbesar(data)

    baris_laporan = [
        "===== LAPORAN PENGELUARAN HARIAN =====",
        f"Jumlah transaksi: {len(data)}",
        f"Total pengeluaran: Rp{total:,}".replace(",", "."),
        f"Rata-rata pengeluaran: Rp{rata_rata:,.0f}".replace(",", "."),
        "",
        "Total berdasarkan kategori:",
    ]

    for nama_kategori, nominal in kategori.items():
        nominal_format = f"Rp{nominal:,}".replace(",", ".")
        baris_laporan.append(f"- {nama_kategori}: {nominal_format}")

    if terbesar:
        nominal_terbesar = f"Rp{terbesar.nominal:,}".replace(",", ".")
        baris_laporan.extend([
            "",
            "Pengeluaran terbesar:",
            f"- {terbesar.keterangan}: {nominal_terbesar}",
        ])

    return "\n".join(baris_laporan)


def simpan_laporan(isi_laporan):
    """Menyimpan laporan ke file teks."""
    import os

    os.makedirs("laporan", exist_ok=True)

    # Mode w menulis laporan baru dan mengganti isi laporan lama.
    with open(FILE_LAPORAN, "w", encoding="utf-8") as file:
        file.write(isi_laporan)
        file.write("\n")
