"""Pengujian otomatis untuk program pengeluaran harian."""

import unittest

from pengeluaran.models import Pengeluaran
from pengeluaran.validasi import (
    validasi_pengeluaran,
    DataTidakValidError,
)
from pengeluaran.processing import (
    hitung_total,
    hitung_rata_rata,
    urutkan_pengeluaran,
)


class TestPengeluaran(unittest.TestCase):
    """Menguji fungsi utama pengeluaran harian."""

    def setUp(self):
        """Menyiapkan data untuk setiap pengujian."""
        self.data1 = Pengeluaran(
            tanggal="10-10-2026",
            kategori="Makan",
            keterangan="Makan siang",
            nominal=20000,
        )

        self.data2 = Pengeluaran(
            tanggal="10-10-2026",
            kategori="Transportasi",
            keterangan="Ongkos bus",
            nominal=10000,
        )

    def test_membuat_pengeluaran(self):
        """Memastikan objek dibuat dengan benar."""
        self.assertEqual(self.data1.nominal, 20000)
        self.assertEqual(self.data1.kategori, "Makan")

    def test_mengubah_data_menjadi_baris(self):
        """Memastikan data dapat diubah menjadi teks."""
        baris = self.data1.ke_baris()
        hasil = Pengeluaran.dari_baris(baris)

        self.assertEqual(hasil.nominal, 20000)
        self.assertEqual(hasil.keterangan, "Makan siang")

    def test_validasi_data_benar(self):
        """Memastikan data yang benar lolos validasi."""
        self.assertTrue(validasi_pengeluaran(self.data1))

    def test_nominal_nol_ditolak(self):
        """Memastikan nominal nol dianggap tidak valid."""
        data = Pengeluaran(
            tanggal="10-10-2026",
            kategori="Makan",
            keterangan="Sarapan",
            nominal=0,
        )

        with self.assertRaises(DataTidakValidError):
            validasi_pengeluaran(data)

    def test_menghitung_total(self):
        """Memastikan total pengeluaran dihitung dengan benar."""
        total = hitung_total([self.data1, self.data2])
        self.assertEqual(total, 30000)

    def test_menghitung_rata_rata(self):
        """Memastikan rata-rata pengeluaran benar."""
        rata_rata = hitung_rata_rata([self.data1, self.data2])
        self.assertEqual(rata_rata, 15000)

    def test_mengurutkan_pengeluaran(self):
        """Memastikan pengeluaran diurutkan dari terbesar."""
        hasil = urutkan_pengeluaran(
            [self.data1, self.data2],
            urutan="terbesar",
        )

        self.assertEqual(hasil[0].nominal, 20000)


if __name__ == "__main__":
    unittest.main()
